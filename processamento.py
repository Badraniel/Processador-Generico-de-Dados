#Localiza uma entrada específica dentro do banco de dados
def localiza(dados, linha):
    quantidade_registros = len(dados)
    if linha < quantidade_registros:
        return dados[linha]
    else:
        raise IndexError('Esse registro não existe')

#Realiza comparações logicas
def comparar(v1, comparador, v2):
    if comparador == '>':
        return v1 > v2
    elif comparador == '>=':
        return v1 >= v2
    elif comparador == '<':
        return v1 < v2
    elif comparador == '<=':
        return v1 <= v2
    elif comparador == '!=':
        return v1 != v2
    elif comparador == '==':
        return v1 == v2

#Devolve apenas as entradas que preenchem condições específicas
def filtrar(dados, coluna, valor, comparacao=None):
    dados_filtrados = []
    for d in dados:
        if not comparacao:
            if d[coluna] == valor:
                dados_filtrados.append(d)
        else:
            if comparar(d[coluna], comparacao, valor):
                dados_filtrados.append(d)
    return dados_filtrados

#Devolve os dados apenas com as colunas requisitadas
def projetar(dados, colunas):
    dados_projetados = []
    for linha in dados:
        linha_projetada = {}
        for campo, valor in linha.items():
            if campo in colunas:
                linha_projetada[campo] = valor
        dados_projetados.append(linha_projetada)
    return dados_projetados
