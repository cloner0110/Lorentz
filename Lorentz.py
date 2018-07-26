import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import pprint

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
  x, y, z = state  # unpack the state vector
  return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # derivatives

state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.01)

states = odeint(f, state0, t)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(states[:,0], states[:,1], states[:,2])
plt.show()
'''
ix=list(),iy=list(),iz=list()
for i in range(1,4001):
	ix(i)=states[i,1]
	iy(i)=states[i,2]
	iz(i)=states[i,3]
print(ix(1))

#sample test : states[1,1] means x at time step one ! 

print(states[1,0])
print(states[1,1])
print(states[1,2])
'''