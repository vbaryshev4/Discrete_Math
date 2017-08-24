# ДОМАШНЕЕ ЗАДАНИЕ:

print("Задача N1: Создать множество А из нечётных чисел от -7 до 7")
A = set()
i = -7
while i != 8: 
	if i % 2 != 0:
		A.add(i)
	i += 1
print("A – множество из нечётных чисел от -7 до 7:", A)
# Копии для задач 3, 4 и 6
A2 = A.copy()
print("A2 - копия множества из нечётных чисел от -7 до 7:", A2)
A3 = A.copy()
print("A3 - копия множества из нечётных чисел от -7 до 7:", A3)
A4 = A.copy()
print("A4 - копия множества из нечётных чисел от -7 до 7:", A4)
print("----")

print("Задача N2: Создать множество В, состоящее из квадратов А")
B = set()
for j in range(len(A)):
	num = A.pop()**2
	B.add(num)
print("В – множество состоящее из квадратов А:", B)
print("----")

print("Задача N3: Создать словарь С, где ключами являются кубы элементов А, а значениями сами элементы")
C = dict()
for j in range(len(A2)):
	elem = A2.pop()
	C.update(C.fromkeys([elem**3], elem))
	# print(z, elem, C)
print("C - словарь: ключи = кубам элементов А2, а значениями сами элементы:", C)
print("----")

print("Задача N4: Создать множество D из пар (элемент А3, элемент объединения элементов В и ключа С")
D = set()
B2 = B.copy()
B2 = (B2.union(set(C.keys())))
# print("B2", B2)
for k in range(len(A3)):
	B3 = B2.copy()
	first_elem = A3.pop()
	for t in range(len(B3)):
		second_elem = B3.pop()
		tpl = (first_elem, second_elem)
		D.add(tpl)
print(D)
print("----")

print("Задача N5: Создать множество Е, из значений словаря С")
E = set(C.values())
print("Е – множество из значений словаря С:", E)
# Копия для задачи 6
E2 = E.copy()
print("Е2 - копия множества Е", E2)
print("----")

print("Задача N6:Найти разность Е и А")
R = set()
R = A4.difference(E2)
print("R - разность Е2 и А4:", R)
print("----")