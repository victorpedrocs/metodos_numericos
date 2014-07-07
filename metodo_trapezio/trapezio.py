# Algoritmo do trapezio

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 1/x

def simpson3( a, b, m):
	

def simpson1( a, b, m ):
	x = np.linspace( a , b, m+1)
	y = f(x)
	h = float( b - a ) / m
	s = f(a) + f(b)

	for i in range( 1, m, 2 ):
		s += 4 * f( a + i * h)
	for i in range( 2, m-1, 2):
		s += 2 * f( a + i * h )

	return s * h / 3 

def trapezio(a, b, s):
	x = np.linspace(a, b, s+1) # retorna um vetor com numeros num intervalo entre a e b com s+1 passos, calculando automaticamente o incremento
	y = f(x)
	soma = sum( y[1:s] )
	h = float( b - a ) / s
	trapezio_composto = h*(	( ( f(a) + f(b) ) / 2 ) + y )

	return sum(trapezio_composto)

def main():
	a = 1
	b = 4
	s = 102
	t = []
	s1 = []
	for i in range(1,s+1):
		t.append( trapezio(a, b, i) )

	for i in range( 1, s+1 ):
		s1.append( simpson1( a, b, i ))


	print "Integral atraves dos trapezios : %10.4f \n" % t[-1]
	print "Integral atraves de Simpson 1/3: %10.4f \n" % s1[-1]

	plt.plot(t)
	plt.plot(s1)

	plt.xlim(0,s)
	plt.show()




main()
