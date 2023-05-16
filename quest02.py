#Escreva um programa que leia uma string e use uma pilha para inverter a ordem das palavras

class Item: 
    def __init__(self, valor): 
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, valor): 
        novoItem = Item(valor)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1
        
    def pop(self): 
        if self.size == 0:
            raise Exception("A pilha está vazia!")
        valor = self.top.valor
        self.top = self.top.next
        self.size -= 1
        return valor
    
    def topo(self):
        if self.size == 0:
            raise Exception ("A pilha está vazia!")
        return self.top.valor

    def is_empty(self): 
        return self.size == 0
    
    def __len__(self):
        return self.size

def inverter(frase):
    palavras = frase.split()
    pilha = Pilha()
    
    for p in palavras:
        pilha.push(p)
    
    NovaFrase = ''
    while not pilha.is_empty(): 
        NovaFrase += pilha.pop() + ' '         
    return NovaFrase

string = input('Digite uma string para descobrir seu inverso: ')
palavra = inverter(string)
print('Palavra inversa: ', palavra)