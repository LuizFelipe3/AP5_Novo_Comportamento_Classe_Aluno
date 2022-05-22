# Conteúdo da ultima aula

from entidades import Aluno

a1 = Aluno('Joãozinho', 1001)
a1.historico.append(10)
a1.historico.append(40)

a2 = Aluno('Matheuszinho', 1002)
a2.historico.append(200)

turma = [a1, a2]

#dashboard
for aluno in turma:
    print(f'[{aluno.registro}] {aluno.nome} : {aluno.getTotal()} h')