# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n < 0 :
		print("ValueError")
	else :
		res = 1
		for i in range(1,n+1) :
			res = res*i 
		return res 
	pass

from math import sqrt

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + c = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	D = b**2 - 4*a*c
	res = []
	if D < 0 :
		pass
	else :
		x = (-b-sqrt(D))/(2*a)
		y = (-b+sqrt(D))/(2*a)
		if x < y :
			res.append(x)
			res.append(y)
		elif x == y :
			res.append(x)
		else :
			res.append(y)
			res.append(x)
	return tuple(res)
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1,1,-2))
	print(roots(1,-2,0))
	print(roots(1, 0, 1))