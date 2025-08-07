# Parental Control Settings: Implementing parental controls for content filtering;
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
    if usuario.perfil.controle_parental is True:
        print("Selecione até que idade você deseja restringir o conteúdo:")
        print("Se você restringir até 10 por exemplo, o usuário não poderá ver conteúdos com classificação indicativa acima de 10 anos")
        print("1. 10 anos")
        print("2. 12 anos")
        print("3. 14 anos")
        print("4. 16 anos")
        print("5. 18 anos")
        opcao = input("Opção: ")
        if opcao == 1:
            idade_limite = 10
        elif opcao == 2:
            idade_limite = 12
        elif opcao == 3:
            idade_limite = 14
        elif opcao == 4:
            idade_limite = 16
        elif opcao == 5:
            idade_limite = 18
        else:
            print("Opção inválida. Tente novamente.")
    else:
        return
