# Algoritmo do trapezio

import numpy as np

def f(x):
	return 1/x

def trapezio(a, b, s):
	x = np.linspace(a, b, s+1) # retorna um vetor com numeros num intervalo entre a e b com s+1 passos, calculando automaticamente o incremento
	y = f(x)

	# print what is going on
	for i in range(n+1):
		print "%5d %10.4f %10.4f" % (i, x[i], y[i])

	integral = y[0] + 2.0 * sum( y[1:n] ) + y[n]
	h = float( b - a ) / s

	return s * h / 2.0

def main():
	a = 1
	b = 4
	s = 6

	t = trapezio(a, b, s)

	print t


main()


