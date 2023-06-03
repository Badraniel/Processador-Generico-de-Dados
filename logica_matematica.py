#Devolve a quantidade de registros na base de dados
def contar(dados):
    return len(dados)

#Soma todos os valores de determinada coluna na base de dados
def somar_registros(coluna, dados):
    total = 0
    for registro in dados:
        total += registro[coluna]
    return total

#Calcula a média de valores de determinada coluna na base de dados
def media(coluna, dados):
    return contar(dados) / somar_registros(coluna, dados)

#Conta quantas vezes um determinado valor aparece na base de dados
def contar_valores_semelhantes(coluna, valor, dados):
    soma = 0
    for registro in dados:
        if registro.get(coluna) and registro.get(coluna) == valor:
            soma += 1
    return soma

#Devolve quantas vezes os valores de determinada coluna da base de dados satisfazem uma comparação a uma referência
def comparar_valores(coluna, comparador, referencia, dados):
    total = 0
    for registro in dados:
        if comparar(registro[coluna], comparador, referencia):
            total += 1
    return total

#Compara dois valores baseado no comparador fornecido
def comparar(v1, v2, comparador):
    comparadores = {'>':lambda v1, v2: v1 > v2, '>=': lambda v1, v2: v1 >= v2,
                    '<': lambda v1, v2: v1 < v2, '<=': lambda v1, v2: v1 <= v2,
                    '!=': lambda v1, v2: v1 != v2, '==': lambda v1, v2: v1 == v2}
    return comparadores[comparador](v1, v2)

