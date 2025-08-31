# Multi-Device Streaming: Enabling content streaming across various devices;

from utility import limpar_tela
import time
import random

class Device:
    def __init__(self, nome, tipo, identificador):
        self.nome = nome
        self.tipo = tipo
        self.identificador = identificador

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - ID: {self.identificador}"

    def notificar_dispositivo(self, mensagem):
        print(f"Notificação enviada para {self.nome}: {mensagem}")

    def exibir_informacoes(self):
        print(f"Dispositivo: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"ID: {self.identificador}")
    
class StreamingSession:
    def __init__(self, usuario):
        self.usuario = usuario
        self.dispositivos = [] 
        self.sessao_ativa = False
        self.perfil_atual = None
        self.midia_atual = None

    def adicionar_dispositivo(self):
        nome = input("Digite o nome do dispositivo: ")
        tipo = input("Digite o tipo do dispositivo: ")
        device_id = random.randint(1000, 9999)

        if any(d.identificador == device_id for d in self.dispositivos):
            print("ID de dispositivo já existe. Gerando um novo ID.")
            device_id = random.randint(1000, 9999)

        dispositivo = Device(nome, tipo, device_id)
        self.dispositivos.append(dispositivo)
        print(f"Dispositivo {dispositivo} adicionado à sessão de streaming.")

    def iniciar_sessao(self):
        if not self.dispositivos:
            print("Nenhum dispositivo disponível para iniciar a sessão.")
            return

        if not self.usuario.perfis:
            print("Nenhum perfil de usuário encontrado. Crie um perfil antes de iniciar a sessão de múltiplo streaming.")
            time.sleep(2)
            limpar_tela()
            return
        
        for p in self.usuario.perfis:
            print(f" - {p.nome_perfil}")

        print("Digite o nome do perfil que deseja usar:")
    
        nome_perfil = input().strip()
        self.perfil_atual = next((p for p in self.usuario.perfis if p.nome_perfil == nome_perfil), None)
        if not self.perfil_atual:
            print("Perfil não encontrado.")
            time.sleep(2)
            limpar_tela()
            return
        
        self.sessao_ativa = True
        self.perfil_atual = nome_perfil
        self.midia_atual = self.usuario.ultimo_conteudo_assistido

        print(f"Sessão de streaming iniciada para o perfil {self.perfil_atual}.")
        if self.midia_atual:
            print(f"Mídia atual: {self.midia_atual}")
            for dispositivo in self.dispositivos:
                dispositivo.notificar_dispositivo(f"Iniciando reprodução de '{self.midia_atual}' no seu dispositivo.")
            input("Pressione Enter para continuar...")
        else:
            print("Selecione algo para assistir antes! A sua última mídia assistida será transmitida no seu dispositivo.")

    def encerrar_sessao(self):
        if not self.sessao_ativa:
            print("Nenhuma sessão ativa para encerrar.")
            return

        self.sessao_ativa = False
        print(f"Sessão de streaming encerrada para o perfil {self.perfil_atual}.")
        self.perfil_atual = None
        self.midia_atual = None
        for dispositivo in self.dispositivos:
            dispositivo.notificar_dispositivo("Sessão de streaming encerrada.")
        input("Pressione Enter para continuar...")

    def remover_dispositivo(self):
        if not self.dispositivos:
            print("Nenhum dispositivo disponível para remover.")
            return

        self.listar_dispositivos()
        try:
            dispositivo_id = int(input("Digite o ID do dispositivo a ser removido: "))
            dispositivo = next(d for d in self.dispositivos if d.identificador == dispositivo_id)
            self.dispositivos.remove(dispositivo)
            print(f"Dispositivo {dispositivo} removido da sessão de streaming.")
        except (ValueError, StopIteration):
            print("ID de dispositivo inválido.")

    def listar_dispositivos(self):
        if not self.dispositivos:
            print("Nenhum dispositivo disponível.")
            return

        print("Dispositivos conectados:\n")
        for dispositivo in self.dispositivos:
            dispositivo.exibir_informacoes()
            print()

    def menu_de_streaming(self):
        while True:
            limpar_tela()
            print("\nConfigurações de Streaming em vários dispositivos:")
            print("╔" + "═" * 50 + "╗")
            print("1. Iniciar Sessão")
            print("2. Encerrar Sessão")
            print("3. Adicionar Dispositivo")
            print("4. Remover Dispositivo")
            print("5. Listar Dispositivos")
            print("6. Sair")
            print("╚" + "═" * 50 + "╝")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.iniciar_sessao()
                time.sleep(2)
            elif opcao == "2":
                self.encerrar_sessao()
                time.sleep(2)
            elif opcao == "3":
                self.adicionar_dispositivo()
                time.sleep(2.5)
            elif opcao == "4":
                self.remover_dispositivo()
                time.sleep(1)
            elif opcao == "5":
                self.listar_dispositivos()
                input("Pressione Enter para continuar...")
            elif opcao == "6":
                print("Saindo do menu de streaming.")
                break
            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(2)
                limpar_tela()
