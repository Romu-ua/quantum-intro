from sympy import *
from sympy.physics.quantum import *
from sympy.physics.quantum.qubit import Qubit, QubitBra

# ベクトル行列をきれいにするため
init_printing()

psi = Qubit('0')
print(psi)
print(represent(psi))

a, b = symbols('alpha, beta')
ket0 = Qubit('0')
ket1 = Qubit('1')
psi = a * ket0 + b * ket1
print(psi)
print(represent(psi))

