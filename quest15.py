#Escreva um progrmaa que leia uma string contendo numeros e use uma pilha para converter a string em um numero binario
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

def Bin(num):
    p = Pilha()
    while num > 0:
        r = num % 2
        num = num // 2
        p.inserir(str(r))
       
    b = ''
    while not p.is_empty():
        b += p.remover()
    if len(b) < 8:
        b = '0' + b
    return b

def converteb(p):
    palavra_b = ''
    
    for i in p:
        y = Bin(ord(i))
        palavra_b += y
        
    return palavra_b

n = input('Digite uma string: ')
bin = converteb(n)
print(bin)