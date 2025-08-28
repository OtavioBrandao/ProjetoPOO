# Bandwidth Optimization: Adapting streaming quality based on user bandwidth
# Nesse caso, estou simulando uma rede instável visto que para fazer isso diretamente teria que importar outras bibliotecas não nativas do python, como o speedtest
import random

class BandaLarga:
    def __init__(self):
        self.velocidade_mbps = None
        self.qualidade_video = "720p" # Qualidade padrão
        self.auto_ajuste = True # Configurado para ajuste automático

    def detectar_velocidade(self):
        return round(random.uniform(0.5, 300), 2) # Retorna um valor aleatório de velocidade de internet
    
    def ajustar_qualidade(self):
        self.auto_ajuste = True
        self.velocidade_mbps = self.detectar_velocidade()
        if self.velocidade_mbps < 0.7:
            print("Mudando para 144p devido à baixa velocidade.")
            self.qualidade_video = "144p"
        elif self.velocidade_mbps < 1.5:
            print("Mudando para 240p devido à baixa velocidade.")
            self.qualidade_video = "240p"
        elif self.velocidade_mbps < 3:
            print("Mudando para 360p devido à baixa velocidade.")
            self.qualidade_video = "360p"
        elif self.velocidade_mbps < 5:
            print("Mudando para 480p devido à baixa velocidade.")
            self.qualidade_video = "480p"
        elif self.velocidade_mbps < 10:
            print("Mudando para 720p devido à média velocidade.")
            self.qualidade_video = "720p"
        elif self.velocidade_mbps < 25:
            print("Mudando para 1080p devido à alta velocidade.")
            self.qualidade_video = "1080p"
        else:
            print("Conexão excelente! Mudando para 4K.")
            self.qualidade_video = "4K"

    def mudar_qualidade(self):
        # Mudar manualmente para a qualidade que eu quiser. Se tentar mudar para resoluções altas com conexão ruim, haverá travamentos
        try: 
            self.auto_ajuste = False
            qualidades_validas = ["144p", "240p", "360p", "480p", "720p", "1080p", "4K"]
            print("As qualidades válidas são:", ", ".join(qualidades_validas))
            print("Digite a qualidade desejada para confirmar a mudança manual:")
            nova_qualidade = input()
            if nova_qualidade in qualidades_validas:
                self.qualidade_video = nova_qualidade
            else:
                print("Qualidade inválida. Escolha entre: 144p, 240p, 360p, 480p, 720p, 1080p, 4K.")

        except:
            print("Qualidade inválida! Continua na configuração anterior.")

    def exibir_configuracoes_qualidade(self):
        print(f"Qualidade de vídeo: {self.qualidade_video}")
        print(f"Ajuste automático: {'Ativado' if self.auto_ajuste else 'Desativado'}")
        print(f"Velocidade da conexão: {self.velocidade_mbps} Mbps")
