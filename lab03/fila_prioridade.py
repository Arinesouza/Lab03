from estrutura_elementar import LinkedList

class prioridade:
    def __init__(self):
        self.dados_prio = LinkedList()
        self.dados = LinkedList()
        
    def enfila(self,valor):
        if valor >= 60:
            self.dados_prio.inserir_inicio(valor)
        else:
            self.dados.inserir_fim(valor)
            
