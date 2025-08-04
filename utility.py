# Benefícios de plano (fazer as funções para o que cada plano pode fazer)
import os
import sys
import unicodedata
import re

def limpar_tela():
    # Limpa a tela do terminal
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def normalizar_texto(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFKD", texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    texto = re.sub(r'\W+', '', texto)  # remove qualquer coisa que não seja letra ou número
    return texto
