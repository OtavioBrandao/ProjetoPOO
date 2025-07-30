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
from library_management import Historico

class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfis = []
        self.plano = "Gratuito" # Plano default ao criar conta

    
    def adicionar_perfil(self, nome, controle_parental=False):
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
        
    # Ver a possibilidade de ver forma de pagamento e tal com o gerenciamento de plano
    def gerenciar_plano(self):
        plano = self.plano
        if plano == "Gratuito":
            print("Seu plano atual é o Gratuito. Deseja mudar para um plano pago?")
            print("1. Mudar para Básico")
            print("2. Mudar para Premium")
            print("3. Manter Gratuito")
            escolha = input()
            if escolha == "1":
                self.plano = "Básico"
                print("Plano mudado para Básico.")
            elif escolha == "2":
                self.plano = "Premium"
                print("Plano mudado para Premium.")
            elif escolha == "3":
                print("Mantendo plano Gratuito.")

        elif plano == "Básico":
            print("Seu plano atual é o Básico. Você tem acesso a recursos limitados.")
            print("Para acessar mais recursos, considere mudar para o plano Premium. Deseja mudar?")
            print("1. Mudar para Premium")
            print("2. Manter Básico")

            escolha = input()
            if escolha == "1":
                self.plano = "Premium"
                print("Plano mudado para Premium.")
            elif escolha == "2":
                print("Mantendo plano Básico.")

        elif plano == "Premium":
            print("Seu plano atual é o Premium. Você tem acesso a todos os recursos.")

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

    def __str__(self):
        return f"Perfil: {self.nome_perfil}, Controle Parental: {'Ativado' if self.controle_parental else 'Desativado'}"