# Parental Control Settings: Implementing parental controls for content filtering;
from utility import limpar_tela
import time

def select_profile_for_parental_control(usuario):
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

def select_profile_for_not_parental_control(usuario):
    while True:
        booleano2 = usuario.listar_perfis()

        if not booleano2:
            return False

        print("Digite o nome do perfil para desativar o controle parental:")
        nome_perfil = input("Nome do perfil: ")

        perfil_encontrado = usuario.obter_perfil_por_nome(nome_perfil)

        if perfil_encontrado:
            usuario.desativar_controle_parental(perfil_encontrado)
            perfil_encontrado.idade_limite = 18  # Resetando a idade limite para o padrão
            perfil_encontrado.catalogo = None  # Resetando o catálogo para o padrão
            break
        else:
            print("Perfil não encontrado. Verifique a sua escrita.\n")
            time.sleep(2)
            limpar_tela()

def restringir_conteudo(usuario):
    perfis_aptos = []

    for perfil in usuario.perfis:
        if perfil.controle_parental is True:
            perfis_aptos.append(perfil)

    if not perfis_aptos:
        print("Nenhum perfil com controle parental ativo!")
        return None

    print("Perfis com controle parental:")
    for i, p in enumerate(perfis_aptos, 1):
        print(f"{i}. {p.nome_perfil}")

    escolha = input("Digite o número do perfil a configurar: ")
    if escolha.isdigit() and 1 <= int(escolha) <= len(perfis_aptos):
        perfil = perfis_aptos[int(escolha) - 1]
    else:
        print("Opção inválida.")
        return None

    print("Deseja personalizar a restrição ou manter a restrição padrão?")
    print("1. Manter padrão")
    print("2. Personalizar restrição")
    escolher = input("Escolha uma opção (1-2): ")

    if escolher == "1":
        personalizar = False
        perfil.idade_limite = 10 # Restrição padrão para crianças
        print("Restrição padrão aplicada: 10 anos")
    elif escolher == "2":
        personalizar = True

    if personalizar is True:

        print("Selecione a idade máxima para restrição:")
        print("1. 12 anos")
        print("2. 14 anos")
        print("3. 16 anos")
        print("4. 18 anos")
        try:
            opcao = input("Escolha uma opção (1-4): ")

            escolhas = {
                "1": 12,
                "2": 14,
                "3": 16,
                "4": 18
            }

            idade = escolhas[opcao]
            perfil.idade_limite = idade
            perfil.catalogo = None
            print(f"Idade limite escolhida: {idade}")

        except KeyError:
            print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
