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

def salvar_arquivo(nome_arquivo, separador, dados):
    f = open(nome_arquivo, 'w')
    string_cabecalho = ''
    cabecalho = list(dados[0].keys())
    for coluna in cabecalho:
        string_cabecalho += f'{coluna}'
        if coluna is not cabecalho[-1]:
            string_cabecalho += f'{separador}'
    string_cabecalho += '\n'
    f.write(string_cabecalho)
    for linha in dados:
        linha_str = ''
        for coluna in linha.keys():
            linha_str += str(linha[coluna])
            if coluna != cabecalho[-1]:
                linha_str += separador
        linha_str += '\n'
        f.write(linha_str)
    f.close()

