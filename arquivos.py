#Formata um documento, devolvendo uma lista de dicionários com cada registro
def formatar_documento(documento, separador, tipos):
    converter = lambda dado, tipo: tipo(dado)
    f = open(documento, 'r')
    linhas = f.readlines()
    cabecalho = linhas[0].rstrip('\n').split(separador)
    doc = []
    for linha in linhas[1:]:
        registro = {}
        dados_linha = linha.rstrip('\n').split(separador)
        for idx, tipo in enumerate(tipos):
            registro[cabecalho[idx]] = converter(dados_linha[idx], tipo)
        doc.append(registro)
    f.close()
    return doc, cabecalho

#Recebe uma lista de registros em dicionário e salva em um documento com um separador
def salvar_documento(nome_documento, separador, dados):
    f = open(nome_documento, 'w')
    cabecalho = list(dados[0].keys())
    string_cabecalho = separador.join(cabecalho) + '\n'
    f.write(string_cabecalho)
    for linha in dados:
        linha_str = separador.join(str(linha[coluna]) for coluna in cabecalho) + '\n'
        f.write(linha_str)
    f.close()