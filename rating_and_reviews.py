# Content Rating and Reviews: Enabling users to rate and review content;
# Provavelmente vou ter que usar a classe usuario para isso, onde um post de um usuario a pode ser visto por um usuario b quando logado em outra conta
from utility import limpar_tela
import time

class Avaliacoes:
    def __init__(self):
        self.avaliacoes = []

    def definir_avaliacao(self, nome, conteudo, nota, comentario):
        avaliacao = {
            "usuario": nome,
            "conteudo": conteudo,
            "nota": nota,
            "comentario": comentario
        }
        self.avaliacoes.append(avaliacao)

    def postar_avaliacao(self, usuario, conteudo):
        print("Postar avaliação:")
        nota = int(input("Digite a nota (1 a 5): "))
        comentario = input("Digite seu comentário sobre o conteúdo: ")
        self.definir_avaliacao(usuario.nome, conteudo, nota, comentario)
        print("Avaliação postada com sucesso!")
        time.sleep(2)
        limpar_tela()

    def mostrar_avaliacoes(self):
        for avaliacao in self.avaliacoes:
            if avaliacao["nota"] == 1:
                avaliacao["nota"] = "★☆☆☆☆"
            elif avaliacao["nota"] == 2:
                avaliacao["nota"] = "★★☆☆☆"
            elif avaliacao["nota"] == 3:
                avaliacao["nota"] = "★★★☆☆"
            elif avaliacao["nota"] == 4:
                avaliacao["nota"] = "★★★★☆"
            elif avaliacao["nota"] == 5:
                avaliacao["nota"] = "★★★★★"
                
            print("═" * 60)
            print("@" + avaliacao["usuario"])
            print("Conteúdo: " + avaliacao["conteudo"])
            print("Nota: " + str(avaliacao["nota"]))
            print("Comentário: " + avaliacao["comentario"])
            print("═" * 60)

    def obter_avaliacoes(self):
        return self.avaliacoes

def processo_para_avaliar(usuario, reviews):
    while True:
        limpar_tela()
        print("O que deseja fazer?")
        print("╔" + "═" * 50 + "╗")
        print("1. Ver avaliações e reviews\n")
        print("2. Fazer uma Review/Avaliação\n")
        print("3. Voltar ao menu principal")
        print("╚" + "═" * 50 + "╝")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            if not reviews.avaliacoes:
                print("Nenhuma avaliação encontrada.")
                time.sleep(2)
                limpar_tela()
                continue
            limpar_tela()
            reviews.mostrar_avaliacoes()
            input("Pressione Enter para continuar...")
            limpar_tela()
        elif opcao == "2":
            limpar_tela()
            if usuario.plano.nome != "Gratuito":
                conteudo = input("Digite o nome do conteúdo que deseja avaliar: ")
                reviews.postar_avaliacao(usuario, conteudo)
            else:
                print("Usuários no plano gratuito não podem postar reviews/avaliações.")
                time.sleep(2)
                limpar_tela()
                continue
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")