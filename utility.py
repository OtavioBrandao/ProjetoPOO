# Benefícios de plano (fazer as funções para o que cada plano pode fazer)
import os
import sys

def limpar_tela():
    # Limpa a tela do terminal
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

