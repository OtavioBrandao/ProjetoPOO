# Parental Control Settings: Implementing parental controls for content filtering;
from user_management import User
from utility import limpar_tela
import time

def activate_parental_control(usuario):
    while True:
        booleano = usuario.listar_perfis()

        if not booleano:
            return False

        print("Digite o nome do perfil para ativar o controle parental:")
        nome_perfil = input("Nome do perfil: ")

        perfil_encontrado = usuario.obter_perfil_por_nome(nome_perfil)

        if perfil_encontrado:
            usuario.ativar_controle_parental(perfil_encontrado)
            break
        else:
            print("Perfil não encontrado. Verifique a sua escrita.\n")
            time.sleep(2)
            limpar_tela()


def deactivate_parental_control(usuario):
    while True:
        booleano2 = usuario.listar_perfis()

        if not booleano2:
            return False

        print("Digite o nome do perfil para desativar o controle parental:")
        nome_perfil = input("Nome do perfil: ")

        perfil_encontrado = usuario.obter_perfil_por_nome(nome_perfil)

        if perfil_encontrado:
            usuario.desativar_controle_parental(perfil_encontrado)
            break
        else:
            print("Perfil não encontrado. Verifique a sua escrita.\n")
            time.sleep(2)
            limpar_tela()

def restringir_conteudo(usuario):
    pass
