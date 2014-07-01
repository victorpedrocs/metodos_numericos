# Algoritmo do trapezio

import numpy as np

def f(x):
	return 1/x

def trapezio(a, b, s):
	x = np.linspace(a, b, s+1) # retorna um vetor com numeros num intervalo entre a e b com s+1 passos, calculando automaticamente o incremento
	y = f(x)

	# print what is going on
	for i in range(s+1):
		print "%5d %10.4f %10.4f" % (i, x[i], y[i])

	soma = sum( y[1:s] )
	
	h = float( b - a ) / s

	integral = y[0] + 2.0 * soma + y[s]

	

	return s * h / 2.0

def main():
	a = 1
	b = 4
	s = 10

	t = trapezio(a, b, s)

	print t


main()
