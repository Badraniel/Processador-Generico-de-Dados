def converte_dados(dado, tipo):
    if tipo == int:
        return int(dado)
    elif tipo == float:
        return float(dado)
    elif tipo == str:
        return str(dado)
    elif tipo == bool:
        if dado == 'True':
            return True
        else:
            return False
    
def carrega_arquivo(nome_arquivo, separador, tipos):
    f = open(nome_arquivo, 'r')
    linhas = f.readlines()
    cabecalho = linhas[0].replace('\n','').split(separador)
    doc = []
    for linha in linhas[1:]:
        registro = {}
        dados_linha = linha.replace('\n','').split(separador)
        for idx, tipo in enumerate(tipos):
            registro[cabecalho[idx]] = converte_dados(dados_linha[idx],tipo)
        doc.append(registro)
    return doc, cabecalho