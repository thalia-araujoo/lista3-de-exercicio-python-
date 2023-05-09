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
        self._toplo = no
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
    
def verificar(exp):
    p = Pilha()
    for i in exp:
        if i == '(':
            p.push(i)
        elif i == ')':
            if p.get_size() > 0:
                p.pop()
            else:
                p.push(i)
    return p.is_empty()
expressao = input('Digite a expressão: ')
if verificar(expressao):
    print('A expressão está balanceada!')
else:
    print('A espressão não está balanceada!')
    
