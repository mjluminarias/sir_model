import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dadt(A,t, beta, gamma, N):
    S = A[0]
    I = A[1]
    R = A[2]
    return [
        -beta/N * S * I,
        beta/N * S * I - gamma * I,
        gamma*I
    ]

times = np.arange(0, 100, 1)
gamma = 1/10
N = 1.1e7
beta = 0.39
S0,I0,R0 = N-574, 574, 0
sol = odeint(dadt, y0=[S0, I0, R0], t=times, args=(beta,gamma,N))

S = sol.T[0]
I = sol.T[1]
R = sol.T[2]

plt.plot(times, S)
plt.plot(times, I)
plt.plot(times, R)
plt.grid()

plt.show()