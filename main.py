class NoArvore:
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

def construirBusca(valores):
    raiz = None
    for valor in valores:
        raiz = inserirBusca(raiz, valor)
    return raiz

def inserirBusca(raiz, valor):
    if not raiz:
        return NoArvore(valor)
    if valor < raiz.valor:
        raiz.esquerda = inserirBusca(raiz.esquerda, valor)
    else:
        raiz.direita = inserirBusca(raiz.direita, valor)
    return raiz

def somaIntervaloBusca(raiz, inicial, final):
    def BuscaemProfundidade(no):
        if not no:
            return 0
        if inicial <= no.valor <= final:
            return no.valor + BuscaemProfundidade(no.esquerda) + BuscaemProfundidade(no.direita)
        elif no.valor < inicial:
            return BuscaemProfundidade(no.direita)
        else:
            return BuscaemProfundidade(no.esquerda)

    return BuscaemProfundidade(raiz)

# Implementacao da interface

valores = list(map(int, input("Digite os valores da arvore sepadados por espacos: ").split()))

raiz = construirBusca(valores)

inicial = int(input("Digite o valor inicial do intervalo: "))

final = int(input("Digite o valor final do intervalo: "))

resultado = somaIntervaloBusca(raiz, inicial, final)

print("A soma dos valores no intervalo [{}, {}] eh {}".format(inicial, final, resultado))



'''
# Exemplo de uso:
valores = [10,5,15,3,7,18]
raiz = construirBusca(valores)

inicial = 7
final = 15
resultado = somaIntervaloBusca(raiz, inicial, final)
print(resultado)
'''



