import sympy as sp 
import random

def GradientMethodWithStepDivision(X0, alpha, beta, f, F):

	X1, X2 = sp.symbols('X1'), sp.symbols('X2')

	def PartialDerivative(X,i):
		var = X1 if i == 1 else X2
		deriv = sp.lambdify((X1,X2), sp.diff(F, var))
		return deriv(X[0],X[1])

	def GradientModule(X):
		return sp.sqrt(PartialDerivative(X,1)**2 + PartialDerivative(X,2)**2)

	def StopCondition(X):
		print(abs(PartialDerivative(X,1)), abs(PartialDerivative(X,2)))
		return abs(PartialDerivative(X,1)) <= delta and abs(PartialDerivative(X,2)) <= delta

	E, delta = 0.5, 0.1
	Xmin = None
	X, Alphas = [], []
	X.append(X0)

	k = 0
	while True:

		if StopCondition(X[k]):
			Xmin = X[k]
			break
		else:
			Alphas.append(alpha)
			X.append([])
			while True:
				for i in range(2):
					if len(X[-1]) < 2:
						X[-1].append(X[k][i] - Alphas[k] * PartialDerivative(X[k], i+1))
					else:
						X[-1][i] = X[k][i] - Alphas[k] * PartialDerivative(X[k], i+1)
				if f(X[k+1]) - f(X[k]) <= -E * Alphas[k] * GradientModule(X[k])**2:
					k += 1
					break
				else:
					Alphas[k] *= beta

	return Xmin



