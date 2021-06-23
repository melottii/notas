import pickle
import sys


def student(notas, alunos): #Função para somar a nota de cada aluno e chamar as ordenações das notas.
    overall_grade, term = [], 0
    for i in notas:
        sum_of_assessments = notas[term][1] + notas[term][2] + notas[term][3] + notas[term][4]
        overall_grade.append((term + 1, sum_of_assessments, notas[term][2], notas[term][5], alunos[term + 1]))
        term += 1
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(overall_grade) + 10))
    quickSort(overall_grade, 0, len(overall_grade)-1)


def quickSort(overall_grade, inf, sup):
    if inf < sup:
        pos = particao(overall_grade, inf, sup)
        quickSort(overall_grade, inf, pos-1)
        quickSort(overall_grade, pos+1, sup)


def particao(overall_grade, inf, sup):
    pivot = overall_grade[inf]
    i= inf+1
    j= sup
    while i<=j:
        while i<=j and overall_grade[i][1] >= pivot[1]:
            i+=1
        while j>=i and overall_grade[j][1] < pivot[1]:
            j-=1
        if i < j:
            overall_grade[i], overall_grade[j] = overall_grade[j], overall_grade[i]
    overall_grade[inf], overall_grade[j] = overall_grade[j], overall_grade[inf]
    print (overall_grade)
    return j


def main():
    with open('entrada.bin', 'rb') as file:
        alunos, notas = pickle.load(file), pickle.load(file)
    student(notas, alunos)


main()