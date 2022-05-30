# 3. Функция шейкерной (коктейльной) сортировки shaker - модификации пузырьковой:
# Цикл 1 – по i от 0 до N/2 :				# i - счетчик пар проходов по списку,
# которых в 2 раза меньше, чем в пузырьковой
# Цикл 2 – по j от i до N-1-i :			# j - номер позиции при проходе по списку слева направо
# Условие – если A[j]>A[j+1] :	# сравнение текущего элемента со следующим
#	Действие – перестановка местами A[j] и A[j+1]
# Цикл 3 – по j от N-2-i до i+1 : 		# j - номер позиции при проходе по списку справа налево
# Условие если A[j]<A[j-1] :		# сравнение текущего элемента с предыдущим
#	Действие – перестановка местами A[j] и A[j-1]

import numpy
from random import randrange

n = (int(input("Введите целое число n: ")))
a = [randrange(1, 100) for i in range(n)]
print(a)


def customSort():
    for i in numpy.arange(0, int(len(a) / 2), 1):
        for j in numpy.arange(0, int(len(a) - 1 - i), 1):
            firstElement = a[j]
            secondElement = a[j + 1]
            if a[j] > a[j + 1]:
                a[j] = secondElement
                a[j + 1] = firstElement
            for j in numpy.arange(len(a) - 2 - i, int(i + 1), 1):
                fElement = a[j]
                sElement = a[j + 1]
                if a[j] < a[j + 1]:
                    a[j] = sElement
                    a[j + 1] = fElement

a.sort(key=customSort())
print(a)
