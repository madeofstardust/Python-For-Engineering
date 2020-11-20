# Ex3
'''
Assume the following system of differential equations, where S is the number of 
susceptible, I the number of infected and R the number of recovered people in a 
population suffering from a virus outbreak. N is the sum of S, I and R. 
Plot the 
graphs for the variables S,I, and R assuming beta = 0.5 and gamma = 0.1 using the 
Forward Euler method to numerically solve the system of ODE for a time period of 
200 days. Assume that at the start of the outbreak we have 1000 susceptible and 
1 infected person. At which day do we have the greatest number of infected? 
Explain what the coefficients beta and gamma represent in the context of a 
virus epidemic. Why is N set equal to the sum of the three variables?

dS/dt  = - (Beta*I*S)/N
dI/dt = ( (Beta*I*S)/N ) - Gamma*I
dR/dt = Gamma * I

Beta = 0.5
Gamma = 0.1
S - susceptible, I - infected, R - recovered
S_0 = 1000
I_0 = 1

N = S + I + R

'''

import numpy as np
import matplotlib.pyplot as plt

#%%
Beta = 0.5
Gamma = 0.1
dt = 1
N_t = 200
t = np.linspace(0, (N_t+1)*dt, N_t+2)
I = np.zeros(N_t+2)
S = np.zeros(N_t+2)
R = np.zeros(N_t+2)
I[0] = 1
S[0] = 1000
R[0] = 0

'''
time = 200
'''    
#%%
for i in range(N_t+1):
    N = S[i]+I[i]+R[i]
    S[i+1] = S[i] + dt*(-1*(Beta*I[i]*S[i]/N))
    I[i+1] = I[i] + dt*(Beta*I[i]*S[i]/N) - Gamma*I[i]
    R[i+1] = R[i] + dt*(Gamma*I[i])
  
#%%
plt.figure()
plt.plot(t, S, 'g-')
plt.plot(t, I, 'r--')
plt.plot(t, R, 'b:')
plt.show()