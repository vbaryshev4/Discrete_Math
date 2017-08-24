R = {(x,y) for x in {"x", "y"} for y in range(1,4)}
print("R – Множество кортежей: ", R)

#####
A = {x for x in range(4,13)}
print("А – Множество в заданном дипазоне: ", A)

#####
S = {x:2+3*(x-1) for x in A}
print("S – Множество A по формуле x:2+3*(x-1): ", S)


####
B = set()
x = 0
while x*x < 24:
	B.add(-x)
	B.add(x)
	x += 1 	

print("В – Множество натуральных чисел: ", B)