# Author: Humberto Vieira de Souza
# LAB 5 de Engenharia Econômica para Software
# Exercício 1:
f = open('exercise1.py', 'r', encoding='utf-8')
file_lines = f.readlines()

print('Total de Linhas Com Comentários e Linhas em Branco', len(file_lines))
for line in file_lines:
    # tirar linhas em Branco e comentários
    if "#" in line or not line:
        file_lines.pop()

print('Total de Linhas Sem Comentários e Linhas em Branco', len(file_lines))


# Exercício 2: https://github.com/alinebrito/eng-software-economica/blob/main/docs/lab-tamanho-sistema-ferramenta-ck.md

# O código base do PyDriller foi Modificado para desconsiderar
# linhas em branco e linhas de comentários adicionadas ou removidas

from exercise2.pydriller.pydriller.metrics.process.lines_count import LinesCount as Loc
from pydriller.metrics.process.lines_count import LinesCount


metric = Loc(
    path_to_repo='https://github.com/ishepard/pydriller.git',
    from_commit='78c9de3349cc97ab25f751229d0f7ad1978e5cde',  # Dez/2022
    to_commit='bfbd501729cfa023917cf41259eeeaa5e548a55a'  # Last Commit
)
print('LOC Sem Condiderar Comentários e Nem Linhas em Branco')
print('Total de Linhas (Adicionadas e Removidas):', metric.count())
print('Total de Linhas Adicionadas:', metric.count_added())
print('Total de Linhas Removidas:', metric.count_removed())


metric = LinesCount(
    path_to_repo='https://github.com/ishepard/pydriller.git',
    from_commit='78c9de3349cc97ab25f751229d0f7ad1978e5cde',  # Dez/2022
    to_commit='bfbd501729cfa023917cf41259eeeaa5e548a55a'  # Last Commit
)
print('LOC Considerando Comentários e Linhas em Branco')
print('Total de Linhas (Adicionadas e Removidas):', metric.count())
print('Total de Linhas Adicionadas:', metric.count_added())
print('Total de Linhas Removidas:', metric.count_removed())

