# Xmin=[0.6224365834165592, 0.6025103533363779] fmin=-3.0324779967620707
import sympy as sp
import random
import colorama

from GradientMethod import GradientMethodWithStepDivision as HelpMethod

colorama.init()

def f(X):
	return -X[0] - 4*X[1]

def condition1(X):
	return -X[0] - X[1]**2 + 1
def condition2(X):
	return X[0] - X[1]

def F(X):
	return f(X) + r * sum([1/condition1(X), 1/condition2(X)])

def SymbolicFunction(r):
	X1, X2, Fsymbolic = [sp.symbols(s) for s in ['X1', 'X2', 'Fsymbolic']]
	Fsymbolic = -X1-4*X2 + r * (1 / (-X1-X2**2+1) + 1 / (X1-X2))
	return Fsymbolic

X0 = []
while not X0:
	X0 = [random.uniform(0.1,10) for i in range(2)]
	if condition1(X0) > 0 and condition2(X0) > 0:
		break
	else:
		X0.clear()

r, c, eps = 10, 12, 0.1
Xmin = None
Xlist = [X0]

k = 0
while True:
	print(f'\nДопоміжна функція {k+1}...')
	Xstar = HelpMethod(Xlist[k], 0.005, 0.7, F, SymbolicFunction(r))
	if condition1(Xstar) >= 0 and condition2(Xstar) >= 0:
		print('точка X* не покинула допустиму область...')
	else:
		break
	delta = r * sum([1/condition1(Xstar), 1/condition2(Xstar)])
	if abs(delta) <= eps:
		Xmin = Xstar
		break
	else:
		r /= c
		Xlist.append(Xstar)
		k += 1

if Xmin:
	fmin = f(Xmin)
	print(colorama.Back.WHITE + f'\nПочаткова точка {X0=}')
	print(f'\n{Xmin=} {fmin=}')
else:
	print('\nПід час обчислень точка Х* покинула допустиму область!')




