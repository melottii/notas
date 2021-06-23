import pickle


def student(notas, alunos): #Função para somar a nota de cada aluno e chamar as ordenações das notas.
    overall_grade, term = [], 0
    for i in notas:
        sum_of_assessments = notas[term][1] + notas[term][2] + notas[term][3] + notas[term][4]
        overall_grade.append((term+1,  sum_of_assessments, notas[term][2], notas[term][5], alunos[term+1]))
        term += 1
    merge_sort(overall_grade), out_formatting(overall_grade)


def merge_sort(overall_grade): #Função para definir os lados e separar os termos para serem comparados.
    if len(overall_grade) > 1:
        middle = len(overall_grade) // 2
        left = overall_grade[:middle]
        right = overall_grade[middle:]
        merge_sort(left)
        merge_sort(right)
        merge(overall_grade, left, right)


def merge(overall_grade, left, right): #Função para comparar e organizar os termos.
    i, j, k = 0, 0, 0
    while (i<len(left)) and (j < len(right)):
        if previous(left[i], right[j]):
            overall_grade[k] = left[i]
            i += 1
        else:
            overall_grade[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        overall_grade[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        overall_grade[k] = right[j]
        j += 1
        k += 1


def previous(left, right): #Função para definir qual termo é maior (define se o termo vai mudar de lugar ou não na merge).
    if left[1] > right[1]:
        return True
    if left[1] < right[1]:
        return False
    if left[2] > right[2]:
        return True
    if left[2] < right[2]:
        return False
    if left[3] < right[3]:
        return True
    if left[3] > right[3]:
        return False
    if left[4] < right[4]:
        return True
    return False


def out_formatting(overall_grade): #Função para definir as maiores notas (5º) e recompensa-los com 2 pontos, além de printar o ranking atualizado.
    ranking = overall_grade[:5]
    for i in range(5, len(overall_grade)):
        if overall_grade[i][1] >= ranking[len(ranking)-1][1] and overall_grade[i][2] >= ranking[len(ranking)-1][2] and overall_grade[i][3] <= ranking[len(ranking)-1][3]:
            ranking.append(overall_grade[i])
    for t in range(len(ranking)):
        t1, t2, t3, t4, t5 = overall_grade[t]
        overall_grade[t] = t1, t2+2, t3, t4, t5
    for m in range(len(overall_grade)):
        print (f'{overall_grade[m][4]} {overall_grade[m][1]}')


def main():
    with open('entrada.bin', 'rb') as file:
        alunos, notas = pickle.load(file), pickle.load(file)
    student(notas, alunos)


main()