import pickle


'''def student(notas, alunos): #Função para somar a nota de cada aluno e chamar as ordenações das notas.
    overall_grade, term = [], 0
    for i in notas:
        sum_of_assessments = notas[term][1] + notas[term][2] + notas[term][3] + notas[term][4]
        overall_grade.append((term+1, sum_of_assessments, notas[term][5]))
        term += 1
    bubblesort(overall_grade, notas, alunos)


def ranking (overall_grade):
    for i in range(len(overall_grade)):
        for j in range(4,len(overall_grade)):



def bubblesort(overall_grade, notas, alunos): #função para ordenar baseado na nota total do aluno.
    for i in range(len(overall_grade)):
        changed = False
        for j in range(0,(len(overall_grade)-i)-1):
            if overall_grade[j][1] < overall_grade[j+1][1]:
                overall_grade[j], overall_grade[j+1] = overall_grade[j+1], overall_grade[j]
                changed = True
        if not changed: return (second_test(overall_grade, notas, alunos))


def second_test(overall_grade, notas, alunos):  #Função para ordenar (Já ordenada no bubble) baseado na segunda nota.
    for i in range(len(overall_grade)):
        for j in range(0, (len(overall_grade)-i)-1):
            if overall_grade[j][1] == overall_grade[j+1][1]:
                if notas[overall_grade[j][0]-1][2] < notas[overall_grade[j+1][0]-1][2]:
                    overall_grade[j], overall_grade[j+1] = overall_grade[j+1], overall_grade[j]
    return (execution(overall_grade, notas, alunos))


def execution(overall_grade, notas, alunos): #função para ordenar (após a ordenação pela segunda nota) baseado no tempo de execução do código.
    for i in range(len(overall_grade)):
        for j in range(0,(len(overall_grade)-i)-1):
            if overall_grade[j][1] == overall_grade[j + 1][1] and \
                    notas[overall_grade[j][0]-1][2] == notas[overall_grade[j+1][0]-1][2]:
                if (overall_grade[j][2]) > (overall_grade[j+1][2]):
                    overall_grade[j], overall_grade[j+1] = overall_grade[j+1], overall_grade[j]
    return (alphabet(overall_grade, notas, alunos))


def alphabet(overall_grade, notas, alunos):
    for i in range(len(alunos)):
        for j in range(0,(len(alunos)-i)-1):
            if overall_grade[j][1] == overall_grade[j + 1][1] and \
                notas[overall_grade[j][0] - 1][2] == notas[overall_grade[j + 1][0] - 1][2] and \
                    (overall_grade[j][2]) == (overall_grade[j+1][2]):
                if alunos[overall_grade[j][0]] > alunos[overall_grade[j+1][0]]:
                    overall_grade[j], overall_grade[j + 1] = overall_grade[j + 1], overall_grade[j]
    return (overall_grade)
'''

def main():
    '''with open('entrada.bin', 'rb') as file:
        alunos, notas = pickle.load(file), pickle.load(file)
    student(notas, alunos)'''
    a = 'a'
    b = 'b'
    if a < b:
        print (a,b)

main()