# Content Library Management: Managing a library of streaming content, including movies and TV shows
from numpy import append
import random
from utility import limpar_tela, normalizar_texto
import time
from abc import ABC, abstractmethod
import datetime
from ads_management import realizar_exibicao_anuncio

class ConjuntoMidias:
    # Referente a varias midias
    def __init__(self):
        self.midias= []
    
    def buscar_por_titulo(self, titulo):
        resultados = []
        titulo = normalizar_texto(titulo)
        for midia in self.midias:
            if titulo in normalizar_texto(midia.titulo):
                resultados.append(midia)
        return resultados if resultados else None

    def buscar_por_genero(self, genero):
        resultados = []
        genero = normalizar_texto(genero)
        for midia in self.midias:
            if genero in normalizar_texto(midia.genero):
                resultados.append(midia)
        return resultados if resultados else None

    def navegar(self, quantidade=5):
        print("\n🎬 Conteúdos sugeridos para você:\n")
        amostra = random.sample(self.midias, min(quantidade, len(self.midias)))
        for midia in amostra:
            midia.exibir_informacoes()
            print()

class Midia(ABC):
    # Referente a uma midia especifica
    def __init__(self, titulo, genero, classificacao, tempo_duracao):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.tempo_duracao = tempo_duracao
        self.assistido = False
        self.ultima_exibicao = None
        

    @abstractmethod
    def exibir_informacoes(self):
        pass

    def configurar_visualizacao(self):
        if self.assistido:
            status = (
                "✔️ Assistido "
                f"(Última exibição: {self.ultima_exibicao.strftime('%d/%m/%Y %H:%M')})"
            )
        else:
            status = "❌ Não Assistido"
        return status
    
    def pular_30_segundos(self):
        pass

    def retomar_30_segundos(self):
        pass

    def central_anuncios(self, usuario):
        pass

    def contar_tempo(self):
        pass

    def assistir(self, usuario):
        usuario.conteudos_vistos += 1
        if usuario.plano.limite_diario < usuario.conteudos_vistos:
            print("Limite diário de visualizações atingido. Assista um anúncio para redefinir esse limite.")
            time.sleep(2)
            limpar_tela()
            
            return
        
        while True:
            limpar_tela()
            titulo = self.titulo.strip()
            titulo_centralizado = titulo.center(24)

            # marcação de estado
            self.assistido = True
            self.ultima_exibicao = datetime.datetime.now()

            # avaliação de banda antes de começar
            usuario.otimizacao_banda_larga.ajustar_qualidade(usuario)
            usuario.otimizacao_banda_larga.exibir_configuracoes_qualidade()
        
            print()

            print("░▀▄░░▄▀")
            print("▄▄▄██▄▄▄▄▄")
            print("█▒░▒░▒░█▀█ Assistindo:")
            print(f"█░▒░▒░▒█▀█ {titulo_centralizado} ")
            print("█▄▄▄▄▄▄███═════════════════════")
            print()
            # A cada alguns segundos, tentar exibir um anuncio
            if usuario.plano.nome != "Premium":
                anuncio = realizar_exibicao_anuncio(usuario)
                if anuncio is True:
                    print("Pressione Enter para continuar.")
                    continue
            else:
                input("Pressione Enter para parar de assistir.")
                limpar_tela()

            print("Conteúdo pausado. O que deseja fazer?")
            escolha = input(
                "1. Continuar assistindo\n"
                "2. Mudar a qualidade de reprodução\n"
                "3. Parar de assistir\n"
                "Escolha uma opção: "
            ).strip()

            if escolha == "1":
                print("Retomando...")
                time.sleep(1)
                continue
            elif escolha == "2":
                usuario.otimizacao_banda_larga.mudar_qualidade(usuario)  
                
            elif escolha == "3":
                print(f"\nVocê parou de assistir {self.titulo}.")
                print("Obrigado por assistir!")
                time.sleep(2)
                limpar_tela()
                break
            else:
                print("Opção inválida.")


    def assistir_convidado(self):
        limpar_tela()
        titulo = self.titulo.strip()
        titulo_centralizado = titulo.center(24)
        self.assistido = True
        self.ultima_exibicao = datetime.datetime.now()

        print("░▀▄░░▄▀")
        print("▄▄▄██▄▄▄▄▄")
        print("█▒░▒░▒░█▀█ Assistindo:")
        print(f"█░▒░▒░▒█▀█ {titulo_centralizado} ")
        print("█▄▄▄▄▄▄███═════════════════════")
        print()
        print("Pressione Enter para parar de assistir.")
        input()
        print(f"\nVocê parou de assistir {self.titulo}.")
        print("Obrigado por assistir!")
        time.sleep(2)
        limpar_tela()


class Filme(Midia):
    def exibir_informacoes(self):
        print("╔" + "═" * 50 + "╗")
        print(f"║ 🎬  {self.titulo:<42}║") 
        print("╠" + "═" * 50 + "╣")
        print(f"║ Tipo: Filme{'':<42}║")
        print(f"║ Gênero: {self.genero:<40}║")
        print(f"║ Classificação: {self.classificacao:<32}║")
        print(f"║ Duração: {self.tempo_duracao} min{'':<31}║")
        print(f"║ Status: {self.configurar_visualizacao()} {'':<31}║")
        print("╚" + "═" * 50 + "╝")

class Serie(Midia):
    def __init__(self, titulo, genero, classificacao, tempo_duracao, episodios, temporadas):
        super().__init__(titulo, genero, classificacao, tempo_duracao)
        self.episodios = episodios
        self.temporadas = temporadas

    def exibir_informacoes(self):
        print("╔" + "═" * 50 + "╗")
        print(f"║ 📺  {self.titulo:<42}║")
        print("╠" + "═" * 50 + "╣")
        print(f"║ Tipo: Série{'':<42}║")
        print(f"║ Gênero: {self.genero:<40}║")
        print(f"║ Classificação: {self.classificacao:<32}║")
        print(f"║ Duração média de episódios: {self.tempo_duracao} min{'':<31}║")
        print(f"║ Episódios: {self.episodios:<40}║")
        print(f"║ Temporadas: {self.temporadas:<38}║")
        print(f"║ Status: {self.configurar_visualizacao()} {'':<31}║")
        print("╚" + "═" * 50 + "╝")

class Documentario(Midia):
    def exibir_informacoes(self):
        print("╔" + "═" * 50 + "╗")
        print(f"║ 📽️  {self.titulo:<42}║")
        print("╠" + "═" * 50 + "╣")
        print(f"║ Tipo: Documentário{'':<42}║")
        print(f"║ Gênero: {self.genero:<40}║")
        print(f"║ Classificação: {self.classificacao:<32}║")
        print(f"║ Duração: {self.tempo_duracao} min{'':<31}║")
        print(f"║ Status: {self.configurar_visualizacao()} {'':<31}║")
        print("╚" + "═" * 50 + "╝")

class Novela(Midia):
    def exibir_informacoes(self):
        print("╔" + "═" * 50 + "╗")
        print(f"║ 🌹  {self.titulo:<42}║")
        print("╠" + "═" * 50 + "╣")
        print(f"║ Tipo: Novela{'':<42}║")
        print(f"║ Gênero: {self.genero:<40}║")
        print(f"║ Classificação: {self.classificacao:<32}║")
        print(f"║ Duração: {self.tempo_duracao} min{'':<31}║")
        print(f"║ Status: {self.configurar_visualizacao()} {'':<31}║")
        print("╚" + "═" * 50 + "╝")

class Anime(Midia):
    def __init__(self, titulo, genero, classificacao, tempo_duracao, episodios, temporadas):
        super().__init__(titulo, genero, classificacao, tempo_duracao)
        self.episodios = episodios
        self.temporadas = temporadas
    def exibir_informacoes(self):
        print("╔" + "═" * 50 + "╗")
        print(f"║ 🎌  {self.titulo:<42}║")
        print("╠" + "═" * 50 + "╣")
        print(f"║ Tipo: Anime{'':<42}║")
        print(f"║ Gênero: {self.genero:<40}║")
        print(f"║ Classificação: {self.classificacao:<32}║")
        print(f"║ Duração média de episódios: {self.tempo_duracao} min{'':<31}║")
        print(f"║ Episódios: {self.episodios:<40}║")
        print(f"║ Temporadas: {self.temporadas:<38}║")
        print(f"║ Status: {self.configurar_visualizacao()} {'':<31}║")
        print("╚" + "═" * 50 + "╝")

    
def todas_as_midias():
    midias = []

    # Ação
    midias.append(Filme("O Resgate", "Ação", "16+", 120))
    midias.append(Filme("Até o Último Homem", "Ação", "16+", 140))
    midias.append(Serie("The Last of Us", "Ação", "16+", 50, 9, 1))
    midias.append(Filme("Vingadores: Ultimato", "Ação", "12", 181))
    midias.append(Serie("The Walking Dead", "Ação", "16", 42, 177, 11))
    midias.append(Serie("Arcane", "Ação", "16", 24, 24, 1))
    midias.append(Filme("Mad Max: Estrada da Fúria", "Ação", "16", 120))
    midias.append(Filme("John Wick", "Ação", "16", 101))
    midias.append(Filme("John Wick 2", "Ação", "16", 122))
    midias.append(Filme("John Wick 3", "Ação", "16", 130))
    midias.append(Filme("Homem-Aranha: Sem Volta para Casa", "Ação", "12", 148))
    midias.append(Filme("Batman: O Cavaleiro das Trevas", "Ação", "12", 152))
    midias.append(Filme("O Resgate do Soldado Ryan", "Ação", "16", 169))
    midias.append(Filme("Stalingrado", "Ação", "16", 131))
    midias.append(Filme("1917", "Ação", "16", 119))
    midias.append(Filme("Invasão do mundo: Batalha de Los Angeles", "Ação", "12", 116))

    # Comédia
    midias.append(Filme("O auto da Compadecida", "Comédia", "12", 100))
    midias.append(Filme("Debi & Loide", "Comédia", "12", 107))
    midias.append(Filme("Shrek 5", "Comédia", "10", 120))
    midias.append(Serie("Brooklyn Nine-Nine", "Comédia", "12", 22, 153, 8))
    midias.append(Serie("Friends", "Comédia", "12", 22, 236, 10))
    midias.append(Serie("Os Simpsons", "Comédia", "10", 22, 700, 34))
    midias.append(Filme("Minecraft: O Filme", "Comédia", "10", 120))
    midias.append(Filme("Minha Mãe é uma Peça", "Comédia", "12", 100))
    midias.append(Serie("The Office", "Comédia", "14", 22, 201, 9))
    midias.append(Filme("Click", "Comédia", "12", 107))

    # Drama
    midias.append(Serie("This Is Us", "Drama", "14", 43, 106, 6))
    midias.append(Filme("A Lista de Schindler", "Drama", "16", 195))
    midias.append(Filme("O Pianista", "Drama", "16", 150))
    midias.append(Serie("Forest Gump", "Drama", "12", 142, 1, 1))
    midias.append(Filme("Oppenheimer", "Drama", "14", 180))
    midias.append(Filme("Ainda Estou Aqui", "Drama", "12", 120))
    midias.append(Filme("A Rede Social", "Drama", "12", 120))
    midias.append(Filme("A Teoria de Tudo", "Drama", "12", 123))
    midias.append(Filme("O Lobo de Wall Street", "Drama", "16", 180))

    # Romance
    midias.append(Filme("A Culpa é das Estrelas", "Romance", "12", 126))
    midias.append(Filme("Como Eu Era Antes de Você", "Romance", "12", 110))
    midias.append(Filme("Atypical", "Romance", "12", 30))
    midias.append(Serie("Thundermans", "Romance", "10", 22, 52, 4))
    midias.append(Filme("Me Chame Pelo Seu Nome", "Romance", "16", 132))
    midias.append(Serie("Emily em Paris", "Romance", "12", 30, 30, 3))
    midias.append(Filme("Para Todos os Garotos que Já Amei", "Romance", "12", 99))

    # Terror
    midias.append(Filme("O Telefone Preto", "Terror", "16", 115))
    midias.append(Filme("Sorria", "Terror", "16", 100))
    midias.append(Filme("O chamado", "Terror", "16", 120))
    midias.append(Filme("Jogos Mortais", "Terror", "18", 90))
    midias.append(Filme("Five Nights at Freddy's", "Terror", "16", 110))
    midias.append(Filme("Five Nights at Freddy's 2", "Terror", "16", 130))

    # Documentário
    midias.append(Documentario("Retratos Fantasmas", "Documentário", "10", 60))
    midias.append(Documentario("Explicando a mente", "Documentário", "10", 30))
    midias.append(Documentario("O Dilema das Redes", "Documentário", "12", 94))
    midias.append(Documentario("Nosso Planeta", "Documentário", "10", 50))
    midias.append(Documentario("O Começo da Vida", "Documentário", "10", 90))
    midias.append(Documentario("Segunda Guerra Mundial em Cores", "Documentário", "10", 50))

    # Animação
    midias.append(Anime("Attack on Titan", "Animação", "16", 24, 75, 4))
    midias.append(Filme("Toy Story 4", "Animação", "10", 100))
    midias.append(Anime("Naruto Shippuden", "Animação", "12", 23, 220, 20))
    midias.append(Anime("One Piece", "Animação", "12", 24, 1000, 20))
    midias.append(Filme("Kung Fu Panda", "Animação", "10", 92))
    midias.append(Serie("Rick and Morty", "Animação", "16", 22, 61, 5))
    midias.append(Serie("Peixonauta", "Animação", "10", 11, 52, 2))
    midias.append(Anime("Dragon Ball Z", "Animação", "12", 24, 291, 9))
    midias.append(Filme("O Rei Leão", "Animação", "10", 88))
    midias.append(Filme("Frozen", "Animação", "10", 102))
    midias.append(Filme("Divertida Mente", "Animação", "10", 95))
    midias.append(Filme("Zootopia", "Animação", "10", 108))
    midias.append(Filme("Sonic: O Filme", "Animação", "10", 99))
    midias.append(Filme("Sonic 2: O Filme", "Animação", "10", 122))
    midias.append(Filme("Super Mario Bros: O Filme", "Animação", "10", 92))
    midias.append(Filme("Minions", "Animação", "10", 91))
    midias.append(Filme("Os Incríveis", "Animação", "10", 115))
    midias.append(Filme("A Era do Gelo", "Animação", "10", 81))
    midias.append(Filme("A Era do Gelo 2", "Animação", "10", 94))
    midias.append(Filme("A Era do Gelo 3", "Animação", "10", 94))
    midias.append(Serie("A Turma da Mônica", "Animação", "10", 11, 52, 2))


    # Fantasia
    midias.append(Serie("Guerra dos Tronos", "Ação", "18", 60, 73, 8))
    midias.append(Filme("Harry Potter e a Pedra Filosofal", "Fantasia", "10", 152))
    midias.append(Filme("O Senhor dos Anéis: A Sociedade do Anel", "Fantasia", "12", 178))
    midias.append(Serie("A casa do Dragão", "Fantasia", "18", 60, 10, 1))
    midias.append(Serie("The Witcher", "Fantasia", "18", 60, 32, 2))
    midias.append(Filme("As Crônicas de Nárnia", "Fantasia", "10", 143))
    midias.append(Filme("Peter Pan", "Fantasia", "10", 77))
    midias.append(Filme("Percy Jackson e o Ladrão de Raios", "Fantasia", "12", 118))

    # Aventura
    midias.append(Serie("Pokémon", "Aventura", "10", 22, 1200, 25))
    midias.append(Serie("Hora de Aventura", "Aventura", "10", 11, 283, 10))
    midias.append(Filme("Jurassic Park", "Aventura", "12", 127))
    midias.append(Serie("Steven Universe", "Aventura", "10", 11, 160, 5))
    midias.append(Serie("Apenas um Show", "Aventura", "10", 11, 261, 8))
    midias.append(Serie("O incrível mundo de Gumball", "Aventura", "10", 11, 240, 6))
    midias.append(Serie("Peppa Pig", "Aventura", "10", 5, 300, 7))
    midias.append(Filme("Como Treinar o Seu Dragão", "Aventura", "10", 98))
    midias.append(Serie("Ben 10", "Aventura", "10", 22, 70, 4))
    midias.append(Serie("Ben 10: Força Alienígena", "Aventura", "10", 22, 70, 4))
    midias.append(Serie("Ben 10: Supremacia Alienígena", "Aventura", "10", 22, 70, 4))
    midias.append(Serie("Ben 10: Omniverse", "Aventura", "10", 22, 70, 4))
    midias.append(Serie("Minecraft: Story Mode", "Aventura", "10", 22, 8, 1))
    
    return midias

def obter_catalogo_do_perfil(perfil) -> ConjuntoMidias:
    if perfil.catalogo is None:
        cat = ConjuntoMidias()
        midias = todas_as_midias()  # cria as instâncias UMA vez para este perfil
        if getattr(perfil, "controle_parental", False):
            midias = [m for m in midias if int(str(m.classificacao).rstrip('+')) <= perfil.idade_limite]
        cat.midias.extend(midias)
        perfil.catalogo = cat
    return perfil.catalogo

# Função principal para assistir o conteúdo
def Explorar_Conteudo(usuario):
    print("Quem está assistindo?")
    continuar = usuario.listar_perfis()
    if not continuar:
        return
    nome_perfil = input("Digite o nome do perfil: ")
    perfil = usuario.obter_perfil_por_nome(nome_perfil) 
    if perfil is None:
        print(f"Perfil '{nome_perfil}' não encontrado. Por favor, tente novamente.")
        return
    print(f"Bem-vindo(a), {perfil.nome_perfil}!\n")

    catalogo = obter_catalogo_do_perfil(perfil)
    
    # Filtro parental
    if perfil.controle_parental:
        catalogo.midias = [m for m in catalogo.midias if int(str(m.classificacao).rstrip('+')) <= perfil.idade_limite]
    
    while True:
        print("Biblioteca de Conteúdo:")
        print("==========================")
        print("1. Buscar por Título")
        print("2. Buscar por Gênero")
        print("3. Navegar pela Biblioteca")
        print("4. Selecionar conteúdo para assistir")
        print("5. Sair")
        print("==========================")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            limpar_tela()
            titulo = input("Digite o título do conteúdo: ")
            resultados = catalogo.buscar_por_titulo(titulo)
            if resultados:
                print("\nResultados da busca por título:\n")
                for midia in resultados:
                    midia.exibir_informacoes()
            else:
                print("Nenhum conteúdo encontrado.")

        elif escolha == "2":
            limpar_tela()
            genero = input("Digite o gênero do conteúdo: ")
            resultados = catalogo.buscar_por_genero(genero)
            if resultados:
                print("\nResultados da busca por gênero:\n")
                for midia in resultados:
                    midia.exibir_informacoes()
            else:
                print("Nenhum conteúdo encontrado.")

        elif escolha == "3":
            limpar_tela()
            catalogo.navegar()
        elif escolha == "4":
            titulo = input("Digite o título do conteúdo que deseja assistir: ")
            resultados = catalogo.buscar_por_titulo(titulo)

            if not resultados:
                print("Conteúdo não encontrado.")
                time.sleep(2)
                limpar_tela()
                continue

            print("\nConteúdos encontrados:\n")
            for idx, midia in enumerate(resultados):
                print(f"[{idx + 1}]")
                midia.exibir_informacoes()
                print()

            escolha_conteudo = input("Digite o número do conteúdo que deseja assistir: ")

            if escolha_conteudo.isdigit():
                indice = int(escolha_conteudo) - 1
                if 0 <= indice < len(resultados):
                    conteudo_escolhido = resultados[indice]
                    usuario.otimizacao_banda_larga.auto_ajuste = True
                    conteudo_escolhido.assistir(usuario)
                    perfil.historico.adicionar_no_historico(conteudo_escolhido)
                    perfil.recomendacoes.adicionar_conteudo(conteudo_escolhido.genero)
                else:
                    print("Opção inválida.")
            else:
                print("Entrada inválida.")


        elif escolha == "5":
            print("Saindo da biblioteca...")
            break

        else:
            print("Opção inválida. Tente novamente.")

def Explorar_Conteudo_Convidado():
    print("Bem-vindo(a) ao modo convidado!")
    catalogo = ConjuntoMidias()
    
    for midia in todas_as_midias():
        catalogo.midias.append(midia)

    while True:
        print("Biblioteca de Conteúdo:")
        print("==========================")
        print("1. Navegar pela Biblioteca")
        print("2. Selecionar conteúdo para assistir")
        print("3. Sair")
        print("==========================")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            limpar_tela()
            # Limitar a navegação para convidados: mostrar apenas 5 conteúdos aleatórios
            catalogo.navegar(quantidade=5)

        elif escolha == "2":
            titulo = input("Digite o título do conteúdo que deseja assistir: ")
            resultados = catalogo.buscar_por_titulo(titulo)

            # Limitar resultados para convidados: mostrar no máximo 3 opções
            if not resultados:
                print("Conteúdo não encontrado.")
                time.sleep(2)
                limpar_tela()
                continue

            resultados_limitados = resultados[:3]

            print("\nConteúdos encontrados (máx. 3):\n")
            for idx, midia in enumerate(resultados_limitados):
                print(f"[{idx + 1}]")
                midia.exibir_informacoes()
                print()

            escolha_conteudo = input("Digite o número do conteúdo que deseja assistir: ")

            if escolha_conteudo.isdigit():
                indice = int(escolha_conteudo) - 1
                if 0 <= indice < len(resultados_limitados):
                    conteudo_escolhido = resultados_limitados[indice]
                    conteudo_escolhido.assistir_convidado()
                else:
                    print("Opção inválida.")
            else:
                print("Entrada inválida.")

        elif escolha == "3":
            print("Saindo da biblioteca...")
            break

        else:
            print("Opção inválida. Tente novamente.")