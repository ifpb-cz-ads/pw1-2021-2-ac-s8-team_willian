#6) Reescreva o programa da abaixo de forma a utilizar for em vez de while.

def soma(L):
	total = 0
	x = 0
	for x in L:
		total+=x
	return total

L = [1, 2, 3]
print(soma(L))