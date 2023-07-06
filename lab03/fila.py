from estrutura_elementar import LinkedList


class fila() :
     def __init__(self):
        self.dados = LinkedList()
     
     def enfila(self,valor):
        self.dados.inserir_inicio(valor)

     def desenfila(self, item):
        self.dados.remove(item)

     def seach(self,item):
        self.dados.procura(item)

