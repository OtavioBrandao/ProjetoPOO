# User Profile Management: Allowing users to create and manage multiple profiles;
# User Subscription Management: Handling user subscriptions, including free trials and payment plans
# Aqui será implementado a criação de contas de usuário e gerenciamento de perfis, com planos e etc.
# Se relaciona com o controle parental também. Essa parte teria (exemplo):
# Criar e deletar contas de usuário
# Fazer login/logout
# Gerenciar plano (gratuito/pago)
# Adicionar e remover perfis (dentro da conta)
# Ativar/desativar controle parental por perfil
from recommendations import Recomendacoes
from bookmarking_and_history import Historico, Marcar
import time
from utility import limpar_tela

class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfis = []
        self.plano = Plano("Gratuito", "R$ 0,00")

    def adicionar_perfil(self, nome, controle_parental=False):

        if len(self.perfis) >= self.plano.maximo_perfis:
            print(f"Limite de perfis atingido. Você só pode ter {self.plano.maximo_perfis} perfis.")
            return
        
        if any(perfil.nome_perfil == nome for perfil in self.perfis):
            print(f"Perfil '{nome}' já existe. Por favor, escolha outro nome.")
            return
        novo_perfil = Perfil(nome, controle_parental)
        self.perfis.append(novo_perfil)
        print(f"Perfil '{nome}' adicionado com sucesso!\n")
    
    def remover_perfil(self, nome):
        for perfil in self.perfis:
            if perfil.nome_perfil == nome:
                self.perfis.remove(perfil)
                print(f"Perfil '{nome}' removido com sucesso!")
                return
            else: 
                print(f"Perfil '{nome}' não encontrado.")

    def obter_perfil_por_nome(self, nome_perfil):
        for perfil in self.perfis:
            if perfil.nome_perfil == nome_perfil:
                return perfil
        return None

    def listar_perfis(self):
        if not self.perfis:
            print("Nenhum perfil encontrado. Deseja adicionar um perfil?")
            print("1. Sim")
            print("2. Não")
            escolha = input()
            
            if escolha == "1":
                nome = input("Digite o nome do novo perfil: ")
                self.adicionar_perfil(nome)
                return True
            if escolha == "2":
                print("Nenhum perfil adicionado.")
                return False
            
        print("Perfis disponíveis:\n")
        for perfil in self.perfis:
            print(perfil, "\n")
        return True

    def login(self, nome, senha):
        if self.nome == nome and self.senha == senha:
            return True
        else:
            return False
        
    def gerenciar_plano(self):
        while True:
            limpar_tela()
            if self.plano.nome == "Gratuito":
                print(f"Plano atual: {self.plano.nome} - {self.plano.preco}")
                self.plano.exibir_beneficios()
                print("\nOpções de Gerenciamento de Plano:")
                print("=========================")
                print("1. Mudar para Básico")
                print("2. Mudar para Premium")
                print("3. Voltar ao menu de configurações")
                print("=========================")
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    self.plano.realizar_pagamento("Básico")
                    limpar_tela()
                elif escolha == "2":
                    self.plano.realizar_pagamento("Premium")
                    limpar_tela()
                elif escolha == "3":
                    print("Voltando ao menu de configurações...")
                    break
                else:
                    print("Opção inválida.")
                time.sleep(2)
                limpar_tela()

            elif self.plano.nome == "Básico":
                print(f"Plano atual: {self.plano.nome} - {self.plano.preco}")
                self.plano.exibir_beneficios()
                print("\nOpções de Gerenciamento de Plano:")
                print("=========================")
                print("1. Mudar para Premium")
                print("2. Cancelar Plano")
                print("3. Voltar ao menu de configurações")
                print("=========================")
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    self.plano.realizar_pagamento("Premium")
                    limpar_tela()
                elif escolha == "2":
                    if self.plano.cancelar_plano() is True:
                        if len(self.perfis) > 5:
                            self.perfis = self.perfis[:5]
                        print("Plano cancelado. Voltando ao plano Gratuito.")
                    else:
                        continue
                elif escolha == "3":
                    print("Voltando ao Menu Principal...")
                    break
                else:
                    print("Opção inválida.")
                time.sleep(2)
                limpar_tela()
            elif self.plano.nome == "Premium":
                print(f"Plano atual: {self.plano.nome} - {self.plano.preco}")
                self.plano.exibir_beneficios()
                print("\nOpções de Gerenciamento de Plano:")
                print("=========================")
                print("1. Cancelar Plano")
                print("2. Voltar ao menu de configurações")
                print("=========================")
                escolha = input("Escolha uma opção: ")
                if escolha == "1":
                    self.plano.cancelar_plano()
                    if len(self.perfis) > 5:
                        self.perfis = self.perfis[:5]
                    print("Plano cancelado. Voltando ao plano Gratuito.")
                    time.sleep(2)
                    limpar_tela()
                elif escolha == "2":
                    print("Voltando ao menu de configurações...")
                    break
                else:
                    print("Opção inválida.")
                time.sleep(2)
                limpar_tela()

    def ativar_controle_parental(self, perfil):
        if perfil in self.perfis:

            if perfil.controle_parental:
                print(f"Controle parental já está ativado para o perfil: {perfil.nome_perfil}")
                return
            
            perfil.controle_parental = True
            print(f"Controle parental ativado para o perfil: {perfil.nome_perfil}")
            return
        else:
            print("Perfil não encontrado.")

    def desativar_controle_parental(self, perfil):
        if perfil in self.perfis:

            if not perfil.controle_parental:
                print(f"Controle parental já está desativado para o perfil: {perfil.nome_perfil}")
                return
            
            perfil.controle_parental = False
            print(f"Controle parental desativado para o perfil: {perfil.nome_perfil}")
            return
        else:
            print("Perfil não encontrado.")

class Perfil:
    def __init__(self, nome_perfil, controle_parental=False):
        self.nome_perfil = nome_perfil
        self.controle_parental = controle_parental
        self.recomendacoes = Recomendacoes()
        self.historico = Historico()
        self.marcar = Marcar()
        self.idade_limite = 18 # idade limite padrão
        self.catalogo = None

    def __str__(self):
        return f"Perfil: {self.nome_perfil}, Controle Parental: {'Ativado' if self.controle_parental else 'Desativado'}"
    
class Plano:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.beneficios = []
        self.anuncios = True 
        self.limite_diario = True
        self.alta_definicao = False
        self.multiplos_dispositivos = False
        self.reviews = False
        self.maximo_perfis = 5
        self.beneficios = [
            "Limite diário de conteúdos",
            "Anúncios frequentes",
            "5 perfis por conta",
            "Avaliar conteúdo"
        ]

    def __str__(self):
        return f"Plano: {self.nome}, Preço: {self.preco}"
    
    def exibir_beneficios(self):
        print(f"Benefícios do plano {self.nome}:")
        for beneficio in self.beneficios:
            print(f" - {beneficio}")

    def plano_gratuito(self):
        self.nome = "Gratuito"
        self.preco = "R$ 0,00"
        self.beneficios = [
            "Limite diário de conteúdos",
            "Anúncios frequentes",
            "5 perfis por conta",
            "Avaliar conteúdo"
        ]
        self.anuncios = True
        self.limite_diario = True
        self.alta_definicao = False
        self.multiplos_dispositivos = False
        self.reviews = False
        self.maximo_perfis = 5

    def plano_basico(self):
        self.nome = "Básico"
        self.preco = "R$ 9,90"
        self.beneficios = [
            "Sem limite diário de conteúdos",
            "Anúncios menos frequentes",
            "Recomendações personalizadas",
            "10 perfis por conta",
            "Reviews e avaliações de conteúdo"
        ]
        self.anuncios = True
        self.limite_diario = False
        self.alta_definicao = False
        self.multiplos_dispositivos = False
        self.reviews = True
        self.maximo_perfis = 10

    def plano_premium(self):
        self.nome = "Premium"
        self.preco = "R$ 39,90"
        self.beneficios = [
            "Acesso a todos os conteúdos",
            "Sem anúncios",
            "Recomendações personalizadas",
            "15 perfis por conta",
            "Conteúdos em alta definição",
            "Streaming em múltiplos dispositivos"
        ]
        self.anuncios = False
        self.limite_diario = False
        self.alta_definicao = True
        self.multiplos_dispositivos = True
        self.reviews = True
        self.maximo_perfis = 15

    def realizar_pagamento(self, nome_plano):
        planos_disponiveis = ["Básico", "Premium"]
        
        if nome_plano not in planos_disponiveis:
            print("Este plano não requer pagamento ou não existe.")
            return

        print(f"Iniciando o pagamento para o plano: {nome_plano}...")
        print("Selecione a forma de pagamento:" \
            "\n1. Cartão de Crédito" \
            "\n2. Boleto Bancário" \
            "\n3. Pix")
        forma_pagamento = input("Digite o número da forma de pagamento: ")
        if forma_pagamento not in ["1", "2", "3"]:
            print("Forma de pagamento inválida. Tente novamente.")
            return
        
        if forma_pagamento == "1":
            print("Pagamento com Cartão de Crédito selecionado.")
        elif forma_pagamento == "2":
            print("Pagamento com Boleto Bancário selecionado.")
        elif forma_pagamento == "3":
            print("Pagamento com Pix selecionado.")

        print(f"Processando pagamento para o plano {nome_plano} com a forma de pagamento selecionada...")
        time.sleep(2)  
        pagamento_aprovado = True  

        if pagamento_aprovado:
            print("Pagamento aprovado!")
            self.trocar_plano(nome_plano)
            print(f"Plano alterado para: {self.nome}")
            time.sleep(3)
        else:
            print("Pagamento recusado. Tente novamente.")
            time.sleep(2)

    def cancelar_plano(self):
        print("Você tem certeza que deseja cancelar o plano?")
        print("Alguns dos benefícios serão perdidos e você voltará ao plano Gratuito.")
        print("Se caso você tiver mais de 5 perfis, eles serão reduzidos para 5.")
        resposta = input("Digite 'sim' para confirmar ou 'não' para cancelar: ")
        if resposta.lower() == "sim":
            self.plano_gratuito()
            time.sleep(2)
            print("Plano cancelado com sucesso.")
        else:
            time.sleep(2)
            print("Cancelamento do plano abortado.")

    def trocar_plano(self, nome):
        if nome == "Gratuito":
            self.plano_gratuito()
        elif nome == "Básico":
            self.plano_basico()
        elif nome == "Premium":
            self.plano_premium()
