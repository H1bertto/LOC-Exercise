# 1. Calcular LOC de um exemplo didático:

# - Crie um projeto trivial, como por exemplo, um programa que exibe uma mensagem
# com o seu nome e a nome disciplina "Engenharia Econômica para Software".

# - Adicione comentários, altere a forma como o posicionamento das chaves é utilizado,
# adicione linhas em branco, etc. Em outras palavras, o seu projeto deve possuir
# diferentes trechos que fazem parte de sistemas do mundo real. Você pode utilizar
# como inspiração os tópicos discutidos neste roteiro.

# - Em seguida, utilize a ferramenta CK para calcular o número de linhas.
# Observe se a ferramenta contabilizou comentários e outros detalhes que você
# adicionou. Você concorda com a forma com o número de linhas foi computado?


# Função para printar seu nome
def print_my_name(name):
    print(f'{name}')


# Função para printar seu nome
def print_course_name(course):
    print(f'{course}')


if __name__ == '__main__':
    print_my_name('Humberto Vieira')
    print_course_name("Engenharia Econômica para Software")

