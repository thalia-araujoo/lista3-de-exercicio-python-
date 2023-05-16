#Escreva um programa que leia uma string contendo números e use uma pilha para converter a string em um número decimal

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1
   
    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
    
    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor

def convererEmDecimal(frase):
    p = Pilha()
    
    for digito in range(len(frase)-1, -1, -1): 
        if frase[digito].isdigit():
            p.inserir(frase[digito])
    
    conversao = ''
    while not p.is_empty():
        conversao += p.remover()
    return conversao

num = (input('Informe a string contendo números que deseja converter para decimal: '))
decimal = convererEmDecimal(num)
print('Em decimal: ', decimal)
    