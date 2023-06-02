from arquivos import carrega_arquivo
from processamento import localiza, filtrar, projetar, acesso_indice, atualizar
import random

alunos, cabecalho = carrega_arquivo('dados/alunos.csv', ',', [str, int, str, float, float, int, float, bool])


#Nestes exemplos, filtramos apenas os alunos da escola Pedro II


def exemplo_filtrar():
    alunos_pedro_ii = filtrar(alunos,'escola','Pedro II','==')
    return alunos_pedro_ii

#Destes, filtramos apenas os que usaram monitoria
def exemplo_filtrar_2():
    alunos_pedro_ii = exemplo_filtrar()
    alunos_monitoria_pedro_ii = filtrar(alunos_pedro_ii, 'monitoria',True)
    return alunos_monitoria_pedro_ii
#Destes, filtramos os que tiraram nota acima de 7 no primeiro semestre

def exemplo_filtrar_3():
    alunos_monitoria_pedro_ii = exemplo_filtrar_2()
    alunos_monitoria_pedro_ii_n7 = filtrar(alunos_monitoria_pedro_ii, 'nota_semestre_1',7,'>')
    return alunos_monitoria_pedro_ii_n7

#Neste exemplo, usamos os dados filtrados anteriormente e acessamos apenas o nome e a note
def exemplo_projetar_3():
    alunos_filtrados = exemplo_filtrar()
    projetado = projetar(alunos_filtrados,['nome','nota_semestre_1'])
    return projetado

#Neste exemplo, localizamos um aluno específico da projeção anterior
def exemplo_localizar():
    dados_projetados = exemplo_projetar_3()
    aluno = localiza(dados_projetados, 0)

#Neste exemplo, criamos uma lista aleatória de alunos do Pedro II e localizamos estes alunos
def exemplo_acesso_índice_específico():
    dados_exemplo = exemplo_filtrar()
    indices = [idx for idx in range(len(dados_exemplo))]
    quantidade_especifica = random.randint(1,len(dados_exemplo))
    indices_acessados = []
    for i in range(0, quantidade_especifica):
        lista = [item for item in indices if item not in indices_acessados]
        indice_escolhido = random.choice(lista)
        indices_acessados.append(indice_escolhido)
    indices_acessados.sort()
    dados_acessados = acesso_indice(dados_exemplo, indices_acessados, 'especifico')
    return dados_acessados

#Neste exemplo, acessamos os índices dos ultimos 10 alunos da lista da monitoria do pedro II
def exemplo_acesso_indice_alcance():
    alunos_monitoria = exemplo_filtrar_3()
    alcance = len(alunos_monitoria)-1
    indices = [alcance-10, alcance]
    dados_acessados = acesso_indice(alunos_monitoria, indices, 'alcance')
    return dados_acessados

#Neste exemplo, todos os alunos do pedroII que faltaram +20 aulas tiraram nota 0 no exame final
def exemplo_atualizar():
    alunos_pedro_ii = exemplo_filtrar()
    alunos_faltosos = filtrar(alunos_pedro_ii, 'faltas', 20, '>')
    alunos_faltosos = atualizar(alunos_faltosos, 'nota_exame', 0)
    return alunos_faltosos

