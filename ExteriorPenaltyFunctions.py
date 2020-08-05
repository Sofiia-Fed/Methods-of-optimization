# Xmin=[1.3429040099267218, 2.692084536998706] fmin=-11.130508917547594
import sympy as sp 
import random
import colorama

from GradientMethod import GradientMethodWithStepDivision as HelpMethod

colorama.init()

def f(X):
	return X[0]**2 + X[1]**2 - 3*X[0] - 6*X[1]

def condition(X):
	return X[0]**2 + X[1]**2 - 9

def F(X):
	return f(X) + r * (max(0, condition(X))**2 + condition(X)**2)

def SymbolicFunction(X,r):
	X1, X2, Fsymbolic, fi = [sp.symbols(s) for s in ['X1', 'X2', 'Fsymbolic', 'fi']]
	fi = X1**2 + X2**2 - 9
	Fsymbolic = X1**2 + X2**2 - 3*X1 - 6*X2 + r * ((2 if condition(X) > 0 else 1) * fi**2)
	return Fsymbolic

X0 = [random.uniform(0.1,10) for i in range(2)]

r, c, eps = 0.01, random.randint(4,10), 0.01
Xmin = None
Xlist = [X0]

k = 0
while True:
	print(f'\nДопоміжна функція {k+1}...')
	Xstar = HelpMethod(Xlist[k], 0.5, 0.75, F, SymbolicFunction(Xlist[k]))
	delta = r * (max(0, condition(Xstar))**2 + condition(Xstar)**2)
	if abs(delta) <= eps:
		Xmin = Xstar
		break
	else:
		r *= c
		Xlist.append(Xstar)
		k += 1

fmin = f(Xmin)
print(colorama.Back.WHITE + f'\nПочаткова точка {X0=}')
print(f'\n{Xmin=} {fmin=}')