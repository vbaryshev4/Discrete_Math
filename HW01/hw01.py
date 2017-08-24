# ДОМАШНЕЕ ЗАДАНИЕ:

print("Задача N1: Создать множество А из нечётных чисел от -7 до 7")
A = {i for i in range(-7,8,2)}
print("A – множество из нечётных чисел от -7 до 7:", A)
print("----")

print("Задача N2: Создать множество В, состоящее из квадратов А")
B = {elem_in_A**2 for elem_in_A in A}
print("В – множество состоящее из квадратов А:", B)
print("----")

print("Задача N3: Создать словарь С, где ключами являются кубы элементов А, а значениями сами элементы")
C = {j**3:j for j in A}
print("C - словарь: ключи = кубам элементов А, а значениями сами элементы:", C)
print("----")

print("Задача N4: Создать множество D из пар (элемент А, элемент объединения элементов В и ключа С")
D = {(j,t) for j in A for t in B.union(set(C.keys()))}
print("D - множество из пар (элемент А, элемент объединения элементов В и ключа С", D)
print("----")

print("Задача N5: Создать множество Е, из ключей словаря С")
E = {i for i in C.keys()}

print("Е – множество из значений словаря С:", E)
print("----")

print("Задача N6:Найти разность Е и А")
R = {i for i in E if i not in A}
Q = {i for i in A if i not in E}
print("E:", E, "\nA", A)
print("R - разность Е и А:", R)
print("Q - разность A и E:", Q)
print("----")