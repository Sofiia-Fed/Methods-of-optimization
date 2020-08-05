import numpy as np

C = np.array([1, 1])
gamma = 4

def f(X):
	return np.log(X[0]**2 + X[1]**2) - X[0] - X[1]

def PartialDerivative(X):
	return [2*X[i] / (X[0]**2 + X[1]**2) - 1 for i in range(2)]

def P(Y):
	return list(Y + ((gamma - sum(C*Y)) / np.linalg.norm(C)**2) * C)

E = 0.001
alpha, beta = 3, 0.7
X0, Xmin = None, None
X = []

#print('Start point : ')
#X0 = [float(input(f'x{i} = ')) for i in range(2)]
X0 = [1.75, 1.83]

X.append(X0)

k = 0
while True:
	X.append([])
	alphaK = alpha
	while True:

		X[k+1] = P(np.array(X[k]) - alphaK*np.array(PartialDerivative(X[k])))

		if f(X[k+1]) - f(X[k]) <= -E * alphaK * np.linalg.norm(np.array(X[k]) - np.array(X[k+1]))**2:
			break
		else:
			alphaK *= beta

	if all(np.array(X[k+1]) - np.array(X[k]) <= E):
		Xmin = X[k]
		break
	else:
		k += 1

print(f'{Xmin = }')
print(f'{f(Xmin) = }')



