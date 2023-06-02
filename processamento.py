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

#Criterio alcance: retorna os indices entre o primeiro e segundo índice da lista no parametro 'indice'
#Criterio específico: retorna cada índice da lista no parametro 'indice'
def acesso_indice(dados, indices, criterio):
    def alcance():
        return [localiza(dados, indice) for indice in range(indices[0], indices[1]+1)]
    def especifico():
        return [localiza(dados, indice) for indice in indices]
    criterios = {'alcance':alcance,
                 'especifico':especifico}
    return criterios[criterio]()

#Devolve os dados com uma modificação numa entrada específica
def atualizar(dados, coluna, modificacao):
    for registro in dados:
        registro[coluna] = modificacao
    return dados

#Devolve os dados que têm o mesmo valor específico em determinada coluna
def agrupar(dados, entrada, valor):
    dados_agrupados = []
    for registro in dados:
        if registro[entrada] == valor:
            dados_agrupados.append(registro)
    return dados_agrupados