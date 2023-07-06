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
            
     def desenfla(self, valor):
         if self.dados_prio is not None:
             self.dados_prio.remove(valor)
         else:
            self.dados.remove(valor)

    def seach(self,item):
         if self.dados_prio is not None:
             self.dados_prio.procura(item)
         else:
            self.dados.remove(item)