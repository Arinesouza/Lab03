from estrutura_elementar import LinkedList


class pilha():
    def __init__(self):
        self.dados = LinkedList()

    def push(self, valor):
       self.dados.inserir_fim(valor)

    def pop(self, item):
        self.dados.remove(item)

    def seach(self,item):
        self.dados.procura(item)






