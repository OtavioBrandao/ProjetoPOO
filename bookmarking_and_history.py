# Bookmarking and Watch History: Allowing users to bookmark content and view their watch history
def ver_historico_de_exibicao(historico):
    historico.exibir_historico()

def limpar_historico(historico):
    historico.limpar_historico()
   
# Ver se da pra colocar a classe histórico aqui

# Para assistir mais tarde
class Marcar:
    def __init__(self, assistido = False):
        self.marcados = []
        self.assistido = assistido

    def marcar_conteudo(self, midia):
        pass
    # Quando o conteúdo for assistido, o assistido vira True e ele não vai aparecer mais no conteúdo marcado
    def desmarcar_conteudo(self, midia):
        pass
    def listar_marcados(self):
        pass

