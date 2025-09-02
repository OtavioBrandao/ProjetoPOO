# Ad Integration and Management: Managing ad placements for ad-supported content.
import random
from utility import limpar_tela
import time
import threading

class Anuncio:
    def __init__(self, nome, produto, descricao):
        self.nome = nome
        self.produto = produto
        self.descricao = descricao

class GerenciarAnuncio:
    def __init__(self): pass

    def exibir_anuncio(self, usuario, banco_ads):
        print("Pressione Enter para pausar.")
        exibido = False
        parar = threading.Event()
        threading.Thread(target=lambda: (input(), parar.set()), daemon=True).start() # Espera pelo Enter
        cont = 0
        passo = 0.5           
        alvo = 30.0          

        while not parar.is_set():
            time.sleep(passo)
            cont += passo

            if cont >= alvo:
                chances = {"Gratuito": 0.65, "Básico": 0.25} 
                mostrar = random.random() < chances.get(usuario.plano.nome, 0.0) # sorteia a chance de 'mostrar' ser true or false

                if mostrar and banco_ads:
                    ad = random.choice(banco_ads)
                    limpar_tela()
                    print("╔" + "═" * 50 + "╗")
                    print(" 📢  ANÚNCIO ESPECIAL")
                    print(f" Nome: {ad.nome:<41}")
                    print(f" Produto: {ad.produto:<38}")
                    print(f" Descrição: {ad.descricao:<35}")
                    print("╚" + "═" * 50 + "╝\n")
                    exibido = True
                    for i in range(3, 0, -1):
                        if parar.is_set(): break   
                        print(f"O anúncio termina em {i}...", end="\r", flush=True)
                        time.sleep(1)
                    print("Anúncio encerrado. Pressione Enter para continuar...")
                cont = 0.0
        return exibido


        


def criar_banco_de_anuncios():
    return [
        Anuncio("SuperFone", "Smartphone X", "O smartphone mais avançado do mercado!"),
        Anuncio("SuperTablet", "Tablet Y", "O tablet mais potente do mercado!"),
        Anuncio("SuperLaptop", "Laptop Z", "O laptop mais leve e rápido do mercado!"),
        Anuncio("SuperWatch", "Smartwatch W", "O smartwatch mais elegante do mercado!"),
        Anuncio("SuperCamera", "Câmera V", "A câmera com a melhor qualidade de imagem!"),
        Anuncio("Coca-Cola", "Refrigerante", "O refrigerante mais famoso do mundo!"),
        Anuncio("Burger King", "Whopper", "Sabor inconfundível que mata a fome!"),
        Anuncio("Nestlé", "Chocolate", "Mais cremoso e delicioso que nunca!"),
        Anuncio("Nike", "Tênis Air Zoom", "Conforto e performance para o seu dia!"),
        Anuncio("Adidas", "Camisa Esportiva", "Leve, respirável e cheia de estilo!"),
        Anuncio("Ray-Ban", "Óculos Aviador", "Clássico que nunca sai de moda!"),
        Anuncio("Spotify", "Premium", "Música sem anúncios, offline e ilimitada!"),
        Anuncio("Netflix", "Plano Padrão", "Séries e filmes para maratonar!"),
        Anuncio("Uber", "Corridas", "Sua viagem rápida e segura a um toque!"),
        Anuncio("PlayStation", "PS5", "O console da nova geração está aqui!"),
        Anuncio("Xbox", "Game Pass", "Milhares de jogos por um café/dia!"),
        Anuncio("Nintendo", "Switch OLED", "Diversão onde você estiver!"),
    ]

def realizar_exibicao_anuncio(usuario):
    banco_ads = criar_banco_de_anuncios()
    anuncio = GerenciarAnuncio()
    return anuncio.exibir_anuncio(usuario, banco_ads)

def redefinir_limite_diario(usuario):
        banco_ads = criar_banco_de_anuncios()
        ad = random.choice(banco_ads)
        limpar_tela()
        print("╔" + "═" * 50 + "╗")
        print(" 📢  ANÚNCIO ESPECIAL")
        print(f" Nome: {ad.nome:<41}")
        print(f" Produto: {ad.produto:<38}")
        print(f" Descrição: {ad.descricao:<35}")
        print("╚" + "═" * 50 + "╝\n")
        usuario.conteudos_vistos = 0


