"""
1-2 量子ビットに対する基本演算
"""
from sympy import *
from sympy.physics.quantum import *
from sympy.physics.quantum.qubit import Qubit, QubitBra

from sympy.physics.quantum.gate import X, Y, Z, H, S, T, CNOT, SWAP, CPHASE

print(X(0))
print(represent(X(0), nqubits=1))
print(represent(H(0),nqubits=1))
print(represent(S(0),nqubits=1))
print(represent(T(0),nqubits=1))
ket0 = Qubit('0')
print(S(0)*Y(0)*X(0)*H(0)*ket0)
print(qapply(S(0)*Y(0)*X(0)*H(0)*ket0))