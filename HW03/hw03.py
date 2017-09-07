# Распечатать матрицу истинности 
# и множество упорядоченных пар для отношения 
# A={1,2,3,4,5,6,7,8,9} 
# B={1,2,3,4,5,6,7,8,9}
# для:
# (x+y)%3 
# x/y

# Конструктор итерратора – [элмент, итерратор, условие]

A={1,2,3,4,5,6,7,8,9} 
B={1,2,3,4,5,6,7,8,9}

R1 = [[True if (x+y)%3==0 else False for y in A]for x in B]
print(R1)
# [[False, True, False, False, True, False, False, True, False], 
#  [True, False, False, True, False, False, True, False, False], 
#  [False, False, True, False, False, True, False, False, True], 
#  [False, True, False, False, True, False, False, True, False], 
#  [True, False, False, True, False, False, True, False, False], 
#  [False, False, True, False, False, True, False, False, True], 
#  [False, True, False, False, True, False, False, True, False], 
#  [True, False, False, True, False, False, True, False, False], 
#  [False, False, True, False, False, True, False, False, True]]

R2 = [[True if x%y==0 else False for y in A]for x in B]
print(R2)
# [[True, False, False, False, False, False, False, False, False],
#  [True, True, False, False, False, False, False, False, False], 
#  [True, False, True, False, False, False, False, False, False], 
#  [True, True, False, True, False, False, False, False, False], 
#  [True, False, False, False, True, False, False, False, False], 
#  [True, True, True, False, False, True, False, False, False], 
#  [True, False, False, False, False, False, True, False, False], 
#  [True, True, False, True, False, False, False, True, False], 
#  [True, False, True, False, False, False, False, False, True]]
