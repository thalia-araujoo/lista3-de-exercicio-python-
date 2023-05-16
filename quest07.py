#Escreva um programa que use uma pilha para converter um número decimal para octal.

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
    
    def peek(self): 
        if self.size == 0:
            raise Exception ("A pilha está vazia!")
        return self.top.valor

    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size

def converter_dec_oct(n):
    p = Pilha()
    q = n
    while n > 0:
        r = n % 8
        n = n // 8
        p.push(r)

    return p

num = int(input('Informe um número para converter para octal: '))
r = converter_dec_oct(num)
while not r.is_empty():
    print(r.pop(), end='')