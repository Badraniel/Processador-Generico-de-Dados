from arquivos import carrega_arquivo
from processamento import localiza, filtrar, projetar

alunos, cabecalho = carrega_arquivo('dados/alunos.csv', ',', [str, int, str, float, float, int, float, bool])

alunos_pedro_ii = filtrar(alunos,'escola','Pedro II','==')

print(len(alunos_pedro_ii))

alunos_monitoria_pedro_ii = filtrar(alunos_pedro_ii, 'monitoria',True)

print(len(alunos_monitoria_pedro_ii))

alunos_monitoria_pedro_ii_n7 = filtrar(alunos_monitoria_pedro_ii, 'nota_semestre_1',7,'>')

projetado = projetar(alunos_monitoria_pedro_ii_n7,['nome','nota_semestre_1'])

aluno = localiza(projetado, 0)
print(aluno)