from logica_matematica import comparar

#Localiza um registro específico na base de dados pelo índice
def localizar(indice, dados):
    quantidade_registros = len(dados)
    if indice < quantidade_registros:
        return dados[indice]
    else:
        raise IndexError('Esse registro não existe')

#Devolve os registros que satisfazem determinada condição
def filtrar(coluna, valor, comparacao, dados):
    dados_filtrados = []
    for d in dados:
        if comparar(d[coluna], valor, comparacao):
            dados_filtrados.append(d)
    return dados_filtrados

#Devolve os dados com apenas as colunas determinadas
def projetar(colunas, dados):
    dados_projetados = []
    for registro in dados:
        linha_projetada = {}
        for coluna, valor in registro.items():
            if coluna in colunas:
                linha_projetada[coluna] = valor
        dados_projetados.append(linha_projetada)
    return dados_projetados

#Devolve registros buscando por índice dependendo do criterio adotado:
#Criterio alcance: recebe uma lista com dois valores, entrega os registros nos índices de um ao outro
#Criterio específico: recebe uma lista de índices, entrega os registros de cada índice
def acesso_indice(indices, criterio, dados):
    def alcance():
        return [localizar(indice, dados) for indice in range(indices[0], indices[1] + 1)]
    def especifico():
        return [localizar(indice, dados) for indice in indices]

    criterios = {'alcance': alcance, 'especifico': especifico}
    return criterios[criterio]()

#Devolve os dados com uma modificacao em determinada coluna
def atualizar(dados, coluna, modificacao):
    for registro in dados:
        registro[coluna] = modificacao
    return dados

#Devolve os dados organizados em um dicionário que tem os items de valor semelhante agrupados sob a mesma chave
def agrupar(coluna, dados):
    dados_agrupados = {}
    for linha in dados:
        valor_celula = linha[coluna]
        if dados_agrupados.get(valor_celula) == None:
            dados_agrupados[valor_celula] = []
        dados_agrupados[valor_celula].append(linha)
    return dados_agrupados

#Cria uma lista com os índices de cada registro em ordem crescente ou decrescente, com base no valor de uma coluna
def ordenar_indices(coluna, crescente, dados):
    indices = list(range(len(dados)))
    indices_ordenados = sorted(indices, key = lambda i:dados[i][coluna], reverse=crescente)
    return indices_ordenados