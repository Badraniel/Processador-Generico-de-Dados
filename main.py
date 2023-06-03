import random
from arquivos import formatar_documento, salvar_documento
from processamento import filtrar, projetar, localizar, acesso_indice, agrupar, atualizar, ordenar_indices
from logica_matematica import somar_registros, media, contar_valores_semelhantes, comparar_valores
arquivo, cabecalho = formatar_documento('dados/alunos.csv', ',', [str, int, str, float, float, int, float, bool])

###Operações mais simples

#Neste exemplo, visualizamos apenas os registros dos alunos da escola Pedro II
def exemplo_filtrar():
    alunos_pedro_ii = filtrar('escola', 'Pedro II', '==', arquivo)
    for i in alunos_pedro_ii:
        print(i)

exemplo_filtrar()
#Neste exemplo, recebemos uma base de dados apenas com o nome do aluno e se utilizou a monitoria
def exemplo_projetar():
    alunos_monitoria = projetar(['nome', 'monitoria'], arquivo)
    for i in alunos_monitoria:
        print(i)

#Neste exemplo, recebemos o primeiro aluno no registro
def exemplo_localizar():
    aluno = localizar(0, arquivo)
    print(aluno)


#Neste exemplo, acessamos alguns alunos de forma aleatória pelos índices no registro
def exemplo_acesso_indice_especifico():
    quantidade_especifica = random.randint(1, len(arquivo))
    indices_acessados = random.sample(range(len(arquivo)), quantidade_especifica)
    indices_acessados.sort()
    dados_acessados = acesso_indice(indices_acessados, 'especifico', arquivo)
    print(dados_acessados)

#Neste exemplo, acessamos os últimos 10 alunos registrados
def exemplo_acesso_indice_alcance():
    alcance = len(arquivo) - 1
    indices = [alcance - 10, alcance]
    dados_acessados = acesso_indice(indices, 'alcance', arquivo)
    print(dados_acessados)

#Neste exemplo, demos nota 0 para todos os alunos que faltaram mais do que 20 aulas
def exemplo_atualizar():
    alunos_faltosos = filtrar('faltas', 20, '>', arquivo)
    alunos_faltosos = atualizar(arquivo, 'nota_exame', 0)
    print(alunos_faltosos)


#Neste exemplo, recebemos os dados agrupados por escola
def exemplo_agrupar():
    escolas = agrupar('escola', arquivo)
    for item in escolas.items():
        print(item)
#Neste exemplo, recebemos uma lista que representa o índice de cada aluno, em ordem de quem faltou mais
#Selecionamos os alunos que menos faltaram
#Projetamos os alunos e a escola
def exemplo_ordenar():
    registros_por_falta = ordenar_indices('faltas', False, arquivo)
    alunos_assiduos = acesso_indice(registros_por_falta[:11], 'especifico', arquivo)
    alunos_assiduos_projetados = projetar(['nome','escola','faltas'], alunos_assiduos)
    print(alunos_assiduos_projetados)

#Neste exemplo, selecionamos os alunos da francisto chagas,
#depois projetamos apenas o nome e as notas
#depois ordenamos o registro em ordem crescente baseada na nota
#Salvamos o arquivo
def exemplo_salvar_arquivo():
    alunos_FC = filtrar('escola','Francisto Chagas', '==', arquivo)
    melhores_alunos_FC_por_notas = projetar(['nome', 'nota_exame'], alunos_FC)
    melhores_notas_alunos_FC = acesso_indice(ordenar_indices('nota_exame', True, melhores_alunos_FC_por_notas),'especifico',melhores_alunos_FC_por_notas)
    salvar_documento('dados/notas_francisto_chagas.csv', ',',melhores_notas_alunos_FC)


#Nestes exemplos, projetamos apenas as faltas e as notas dos alunos
#para receber o total de faltas registradas, a média das notas, quantas provas foram zeradas
#e quantas ficaram acima da média
def exemplos_logica_matematica():
    documento = projetar(['faltas','nota_exame'], arquivo)
    numero_faltas = somar_registros('faltas', documento)
    media_notas = media('nota_exame', documento)
    provas_zeradas = contar_valores_semelhantes('nota_exame', 0, documento)
    provas_acima_media = comparar_valores('nota_exame', '>=', 7, documento)
    print(f'Numero de faltas: {numero_faltas}\n'
          f'Média de notas: {media_notas}\n'
          f'Provas Zeradas: {provas_zeradas}\n'
          f'Acima da média: {provas_acima_media}')


