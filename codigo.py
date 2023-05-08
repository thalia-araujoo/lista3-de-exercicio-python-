Class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def is_empty(self):
        return self.tamanho == 0

    def inserir(self, valor):
        No = no(valor)
        No.proximo = self.topo
        self.topo = No
        self.tamanho += 1

    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -+ 1
        return valor

    def _top(self):
        if self.size == 0:
            raise Exception("A pilha está vazia")
        return self.top.valor
#quest 3

def calcular(exp):
    p = pilha()
    for caractere in exp:
        if caractere.isdigit():
            p.insert(caractere)
        else:
            num2 = p.remover()
            num1 = p.remover()
        if caractere == '+':
            resultado = int(nume1) + int(num2)
            p.inserir(str(resultado))
        elif caractere == '-':
            resultado = int(num1) - int(num2)
            p.insert(str(resultado))
        elif caractere == '*':
            resultado = int(num1) * int(num2)
            p.insert(str(resultado))
        elif caractere == '/':
            resultado = int(num1) / int(num2)
            p.insert(str(resultado))
    return p.remover()