import time
from user_management import User
from parental_control import select_profile_for_parental_control, select_profile_for_not_parental_control, restringir_conteudo
from utility import limpar_tela
from library_management import Explorar_Conteudo, Explorar_Conteudo_Convidado
from bookmarking_and_history import ver_historico_de_exibicao, limpar_historico
from rating_and_reviews import Avaliacoes, processo_para_avaliar

# Video Streaming Service - Main Module

usuarios_registrados = []  # Lista para armazenar usuários registrados
reviews = Avaliacoes()

def inicializar():
    limpar_tela()
    print("═"*20)
    print("VSTREAMING HUB")
    print("═"*20)

def criar_conta():
    print("Digite o nome do usuário:")
    nome = input()
        # Verifica se o usuário já existe
    for usuario in usuarios_registrados:
        if usuario.nome == nome:
            print("Usuário já existe. Tente novamente.")
            return criar_conta()
        
    print("Digite seu email:")
    email = input()
        # Verifica se o email já está registrado
    for usuario in usuarios_registrados:
        if usuario.email == email:
            print("Esse email já foi registrado. Tente novamente.")
            return criar_conta()
        
    print("Digite sua senha:")
    senha = input()
    print("Confirme sua senha:")
    senha2 = input()

    # Verifica se as senhas coincidem
    if senha == senha2:
        novo_usuario = User(nome, email, senha) # Instancia de um novo usuário que será adicionado à lista
        usuarios_registrados.append(novo_usuario)
        print("Sua conta foi criada com sucesso!")
    else:
        print("As senhas não coincidem. Tente novamente.")
        criar_conta()

def fazer_login(usuarios_registrados):
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios_registrados:
        if usuario.login(nome, senha):
            print(f"Login bem-sucedido! Bem-vindo, {usuario.nome}.")
            return usuario

    print("Usuário ou senha incorretos.")
    print("1. Tentar novamente")
    print("2. Voltar ao menu inicial")
    opcao = input("Escolha uma opção (1-2):\n ")
    if opcao == "1":
        limpar_tela()
        return fazer_login(usuarios_registrados)
    elif opcao == "2":
        limpar_tela()
        menu_inicial()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
        limpar_tela()
        return fazer_login(usuarios_registrados)

def menu_inicial():
    print("Bem-vindo ao VStreamingHub!\n")
    print("Deseja criar uma conta ou fazer login?\n")
    print("===========================")
    print("1. Criar conta\n")
    print("2. Fazer login\n")
    print("3. Continuar como convidado\n")
    print("4. Sair")
    print("===========================")

    opcao = input("Escolha uma opção (1-4):\n ")
    if opcao == "1":
        limpar_tela()
        criar_conta()
        time.sleep(2)
        limpar_tela()
        menu_inicial()
        
    elif opcao == "2":
        limpar_tela()
        menu_principal()
    elif opcao == "3":
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "4":
        print("Saindo do Video Streaming Service. Até logo!\n")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
        limpar_tela()
        menu_inicial()

def menu_config_usuario(usuario):
    while True:
        print("Configurações de usuário:\n")
        print("==========================================")
        print("1. Gerenciar meus perfis\n")
        print("2. Gerenciar meu plano de assinatura\n")
        print("3. Configurações de controle parental\n")
        print("4. Voltar ao menu principal")
        print("==========================================")

        opcao_usuario = input("Escolha uma opção (1-4):\n ")
        
        if opcao_usuario == "1":       
        #Aplicando o módulo de listar perfis feito no user_management 
            limpar_tela()
            if usuario.listar_perfis():
                print("Deseja adicionar ou remover um perfil?")
                print("1. Adicionar perfil")
                print("2. Remover perfil")
                print("3. Voltar ao menu de configurações")
                escolha_perfil = input("Escolha uma opção (1-3):\n ")

                if escolha_perfil == "1":
                    limpar_tela()
                    nome_perfil = input("Digite o nome do novo perfil: ")
                    usuario.adicionar_perfil(nome_perfil)
                    time.sleep(2)
                    limpar_tela()
                elif escolha_perfil == "2":
                    limpar_tela()
                    print("Perfis disponíveis para remoção:")
                    usuario.listar_perfis()
                    nome_perfil = input("Digite o nome do perfil a ser removido: ")
                    usuario.remover_perfil(nome_perfil)
                    time.sleep(2)
                    limpar_tela()
                elif escolha_perfil == "3":
                    limpar_tela()
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
            else: 
                limpar_tela()
                menu_config_usuario(usuario)
        elif opcao_usuario == "2":
            limpar_tela()
            usuario.gerenciar_plano()
            time.sleep(2)
            limpar_tela()
        elif opcao_usuario == "3":

            limpar_tela()

            while True:
                print("Configurações de Controle Parental:\n")
                print("==========================================")
                print("Você pode ativar o controle parental para um perfil existente ou restringir conteúdo.")
                print("1. Ativar controle parental")
                print("2. Desativar controle parental")
                print("3. Restrição de conteúdo")
                print("4. Voltar ao menu de configurações")
                print("==========================================")
                escolha = input("Escolha uma opção (1-4):\n ")

                if escolha == "1":
                    limpar_tela()

                    while True:
                        limpar_tela()
                        outro_perfil = select_profile_for_parental_control(usuario)
                        time.sleep(2)
                        if outro_perfil:
                            print("Deseja ativar o controle parental para outro perfil?" \
                                "\n1. Sim\n2. Não")
                            escolha_controle = input("Escolha uma opção (1-2):\n ")

                            if escolha_controle == "1":
                                limpar_tela()
                                continue  # volta para o início do loop e ativa para outro perfil
                            elif escolha_controle == "2":
                                limpar_tela()
                                break  # sai do loop e volta ao menu_config_usuario
                            else:
                                print("Opção inválida. Tente novamente.")
                                time.sleep(2)
                        else:
                            
                            limpar_tela()
                            break
                elif escolha == "2":
                    limpar_tela()
                    select_profile_for_not_parental_control(usuario)
                    time.sleep(2)
                    limpar_tela()
                elif escolha == "3":
                    limpar_tela()
                    restringir_conteudo(usuario)
                    time.sleep(2)
                    limpar_tela()
                elif escolha == "4":
                    limpar_tela()
                    break
                else:
                    print("Opção inválida. Tente novamente.")
                    time.sleep(2)
                    limpar_tela()

        elif opcao_usuario == "4":
            limpar_tela()
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            limpar_tela()

def menu_principal_convidado():
    print("Bem-vindo, convidado!\n"
          "Você pode explorar o conteúdo, porém o resto das funcionalidades estão limitadas. Crie uma conta para ter acesso completo aos nossos serviços.\n"
          "O que você gostaria de fazer?\n"
          )
    print("==============================================")
    print("1. Consultar biblioteca de conteúdo\n")
    print("2. Voltar ao menu inicial")
    print("==============================================")

    opcao = input("Escolha uma opção (1-2):\n ")
    if opcao == "1":
        limpar_tela()
        print("Consultando biblioteca de conteúdo...\n")
        time.sleep(2)
        limpar_tela()
        Explorar_Conteudo_Convidado()
        print("Você pode criar uma conta para acessar mais funcionalidades.\n")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()
    elif opcao == "2":
        limpar_tela()
        menu_inicial()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
        limpar_tela()
        menu_principal_convidado()


def menu_principal(usuario=None):
    limpar_tela()
    if usuario is None:
        usuario = fazer_login(usuarios_registrados)
    limpar_tela()

    print(f"Bem-vindo ao Video Streaming Service, {usuario.nome}!\n"
          "O que você gostaria de fazer?\n"
          )
    print("==============================================")
    print("1. Consultar biblioteca de conteúdo\n")
    print("2. Configurações de usuário\n")
    print("3. Recomendações personalizadas\n")
    print("4. Streaming em múltiplos dispositivos\n")
    print("5. Otimização de banda larga\n")
    print("6. Marcar conteúdo e histórico de visualização\n")
    print("7. Revisões e avaliações de conteúdo\n")
    print("8. Integração com anúncios\n")
    print("9. Logout")
    print("==============================================")

    opcao = input("Escolha uma opção (1-9):\n ")

    if opcao == "1":
        limpar_tela()
        print("Consultando biblioteca de conteúdo...\n")
        time.sleep(2)
        limpar_tela()
        Explorar_Conteudo(usuario)
        menu_principal(usuario)
    elif opcao == "2":
        limpar_tela()
        menu_config_usuario(usuario)
        menu_principal(usuario)

    elif opcao == "3":
        limpar_tela()
        print("Selecione o perfil para visualizar recomendações personalizadas:\n")
        usuario.listar_perfis()
        nome_perfil = input("Digite o nome do perfil: ")
        perfil = usuario.obter_perfil_por_nome(nome_perfil)

        if perfil:
            perfil.recomendacoes.recomendar_conteudo()
        else:
            print("Perfil não encontrado.")

        time.sleep(2)
        limpar_tela()
        menu_principal(usuario)
    elif opcao == "4":
        #implementar funcao streaming_multiplos_dispositivos()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal(usuario)
    elif opcao == "5":
        #implementar funcao otimizacao_banda_larga()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal(usuario)
    elif opcao == "6":
        limpar_tela()
        while True:
            print("Marcação de conteúdo e histórico de visualização:\n")
            print("==========================================")
            print("1. Ver histórico de exibição\n")
            print("2. Limpar histórico de exibição\n")
            print("3. Marcar conteúdo\n")
            print("4. Voltar ao menu principal")
            print("==========================================")
            opcao_historico = input("Escolha uma opção (1-4):\n ")
            if opcao_historico == "1":
                limpar_tela()
                print("Selecione o perfil para acessar o histórico:\n")
                usuario.listar_perfis()
                nome_perfil = input("Digite o nome do perfil: ")
                perfil = usuario.obter_perfil_por_nome(nome_perfil)

                if perfil:
                    ver_historico_de_exibicao(perfil.historico)
                    input("Pressione Enter para voltar...")
                else:
                    print("Perfil não encontrado.")
                limpar_tela()
                continue 
        
            elif opcao_historico == "2":
                print("Selecione o perfil para acessar o histórico:\n")
                usuario.listar_perfis()
                nome_perfil = input("Digite o nome do perfil: ")
                perfil = usuario.obter_perfil_por_nome(nome_perfil)

                if perfil:
                    limpar_historico(perfil.historico)
                    print("Histórico de exibição limpo com sucesso!\n")
                    input("Pressione Enter para continuar...")
                else:
                    print("Perfil não encontrado.")
                limpar_tela()
                continue
            elif opcao_historico == "3":
                print("Marcação de conteúdo ainda não implementada.\n")
                input("Pressione Enter para continuar...")
                limpar_tela()
            elif opcao_historico == "4":
                break   
        limpar_tela()
        menu_principal(usuario)
    elif opcao == "7":
        processo_para_avaliar(usuario, reviews)
        limpar_tela()
        menu_principal(usuario)
    elif opcao == "8":
        #implementar funcao integracao_anuncios()
        print("Não implementado\n")
        time.sleep(2)
        limpar_tela()
        menu_principal(usuario)
    elif opcao == "9":
        limpar_tela()
        print("Você escolheu sair.\n")
        print("Tem certeza de que deseja sair?\n"
              "1. Sim\n"
              "2. Não\n")
        opcao_logout = input("")
        if opcao_logout == "1":
            print("Desconectando...\n")
            time.sleep(2)
            limpar_tela()
            menu_inicial()
        elif opcao_logout == "2":
            print("Retornando ao menu principal...\n")
            time.sleep(2)
            limpar_tela()
            menu_principal(usuario)
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            limpar_tela()
            menu_principal(usuario)
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(2)
        limpar_tela()
        menu_principal(usuario)

if __name__ == "__main__":
    inicializar()
    menu_inicial()
