import math
import matplotlib.pyplot as plt
import numpy as np

print("*******INFLOW PERFORMANCE RELATIONSHIP*******\n")
k = float(input("Enter permeability of payzone (in mD) : "))
h = float(input("Enter the thickness of payzone (in ft) : "))
pr = float(input("Enter reservoir pressure (in psi) : "))
pb = float(input("Enter bubble point pressure (in psi) : "))
rw = float(input("Enter well radius (in ft) : "))
re = float(input("Enter drainage radius (in ft) : "))
u = float(input("Enter viscosity (in cp) : "))
bo = float(input("Enter oil formation volume factor (in rbl/stb) : "))
s = float(input("Enter skin factor : "))

if pr == pb:
    print("\nGiven reservoir is saturated reservoir")
    j = (k*h)/(141.2*bo*u*(math.log(((0.472*re/rw) + s), math.e)))
    q_max = j*pr/1.8
    print("maximum flow rate is ", round(q_max, 2), "STB/day")
    n = int(input("\nEnter number of pressure readings : "))
    Q = []
    PWF = []
    for i in range(n):
        pwf = float(input(f"Pwf{i+1} : "))
        q = q_max*(1-(0.2*pwf/pr)-(0.8*((pwf/pr)**2)))
        PWF.append(pwf)
        Q.append(round(q, 2))
    x = np.array(Q)
    y = np.array(PWF)
    plt.plot(x, y)
    plt.title("IPR : SINGLE PHASE FLOW")
    plt.xlabel("Q (in STB/day)")
    plt.ylabel("Pwf (in psi)")
    plt.grid(alpha=.4, linestyle='--')
    plt.show()

elif pr > pb:
    print("\nGiven reservoir is unsaturated reservoir")
    j = (k * h) / (141.2 * bo * u * (math.log(((0.472 * re / rw) + s), math.e)))
    qb = j*(pr-pb)
    qv = j*pb/1.8
    print("flow rate at bubble point pressure is ", round(qb, 2), "STB/day")
    n = int(input("\nEnter number of pressure readings : "))
    Q = []
    PWF = []
    for i in range(n):
        pwf = float(input(f"Pwf{i+1} : "))
        q = qb + (qv * (1 - (0.2 * pwf / pr) - (0.8 * ((pwf / pr) ** 2))))
        PWF.append(pwf)
        Q.append(round(q, 2))
    x = np.array(Q)
    y = np.array(PWF)
    plt.plot(x, y)
    plt.title("IPR : TWO PHASE PARTIAL FLOW")
    plt.xlabel("Q (in STB/day)")
    plt.ylabel("Pwf (in psi)")
    plt.grid(alpha=.4, linestyle='--')
    plt.show()
