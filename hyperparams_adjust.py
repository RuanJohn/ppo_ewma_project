import sympy as sp
import random
import math

learning_rate = 5e-4
a_beta1 = 0.9
a_beta2 = 0.999
b_prox = 0.889
c = 8

# symbol
b = sp.symbols('b')

equation = c * ((1/(1-b_prox)-1)) - ((1/(1-b))-1)

# solve for 'b'
solutions = sp.solve(equation, b)

# print adjusted hyperparamerters
print('Adjusted hyperparams')
print("beta_prox={:.4f}".format(solutions[0]))
print("learning_rate={:.6f}".format(learning_rate / math.sqrt(c)))
print("a_beta1={:.3f}".format(a_beta1 ** (1/c)))
print("a_beta2={:.3f}".format(a_beta2 ** (1/c)))