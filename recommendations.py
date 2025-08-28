# Personalized Recommendations: Offering personalized content recommendations based on user preferences
import time


class Recomendacoes:
    def __init__(self):
        #self.nome = nome (ver o que fazer com isso, se for usar o nome do filme aq)
        self.conteudos = []

    def adicionar_conteudo(self, nome):
        self.conteudos.append(nome)

    def recomendar_conteudo(self):
        contador_acao = contador_comedia = contador_drama = 0
        contador_romance = contador_terror = contador_documentario = 0
        contador_animacao = contador_fantasia = contador_aventura = 0

        if not self.conteudos:
            print("Assista algo para poder ter recomendações relacionadas ao seu gosto!")
            time.sleep(2)
            return
        else:
            for conteudo in self.conteudos:
                if conteudo == "Ação":
                    contador_acao += 1
                elif conteudo == "Comédia":
                    contador_comedia += 1
                elif conteudo == "Drama":
                    contador_drama += 1
                elif conteudo == "Romance":
                    contador_romance += 1
                elif conteudo == "Terror":
                    contador_terror += 1
                elif conteudo == "Documentário":
                    contador_documentario += 1
                elif conteudo == "Animação":
                    contador_animacao += 1
                elif conteudo == "Fantasia":
                    contador_fantasia += 1
                elif conteudo == "Aventura":
                    contador_aventura += 1

        maximo = max(contador_acao, contador_comedia, contador_drama, contador_romance,
                     contador_terror, contador_documentario, contador_animacao,
                     contador_fantasia, contador_aventura)
        # Implementar função aqui pra retornar uma lista de filmes ou series de uma categoria específica
        # Exemplo: retornar lista de filmes de ação
        if maximo == contador_acao:
            print("Recomendação: Ação")
        elif maximo == contador_comedia:
            print("Recomendação: Comédia")
        elif maximo == contador_drama:
            print("Recomendação: Drama")
        elif maximo == contador_romance:
            print("Recomendação: Romance")
        elif maximo == contador_terror:
            print("Recomendação: Terror")
        elif maximo == contador_documentario:
            print("Recomendação: Documentário")
        elif maximo == contador_animacao:
            print("Recomendação: Animação")
        elif maximo == contador_fantasia:
            print("Recomendação: Fantasia")
        elif maximo == contador_aventura:
            print("Recomendação: Aventura")
