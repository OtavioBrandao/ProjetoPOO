from user_management import User, Perfil
from rating_and_reviews import Avaliacoes


# Preencher com coisas predefinidas
usuarios_predefinidos = []

usuario1 = User("João", "joao@example.com", "senha123")
usuario2 = User("Maria", "maria@example.com", "senha456")
usuario3 = User("José", "jose@example.com", "senha789")
usuario4 = User("Teste", "teste@example.com", "123456")
usuario5 = User("Otávio", "otaviomenezes574@gmail.com", "senha1234")

usuario4.adicionar_perfil("Adulto", controle_parental=False)
usuario4.adicionar_perfil("Criança", controle_parental=True)
usuario5.adicionar_perfil("Otávio", controle_parental=False)

avaliacoes_predefinidas = Avaliacoes() # Avaliações já predefinidas que podem ser usadas para adicionar mais
avaliacoes_predefinidas.definir_avaliacao(usuario1.nome, "O Telefone Preto","★★★★★", "Excelente filme!")
avaliacoes_predefinidas.definir_avaliacao(usuario2.nome, "O Poderoso Chefão", "★★★★☆", "Muito bom, mas poderia ser melhor.")
avaliacoes_predefinidas.definir_avaliacao(usuario3.nome, "A Origem", "★★★☆☆", "Ok, nada especial.")
avaliacoes_predefinidas.definir_avaliacao(usuario4.nome, "Titanic", "★★☆☆☆", "Não gostei.")

usuarios_predefinidos = [
    usuario1,
    usuario2,
    usuario3,
    usuario4,
    usuario5
]

def retornar_usuarios_predefinidos():
    return usuarios_predefinidos

def retornar_avaliacoes_predefinidas():
    return avaliacoes_predefinidas