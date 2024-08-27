from random import choice, shuffle
alunos = input('Escreva o nome dos alunos separados por vírgula: ').split(", ")
#shuffle(list)
#list = [alunos]
#print(F"a equecia exvolhida foi {shuffle(alunos)}")
print('O aluno escolhido foi: {}'.format(choice(alunos)))