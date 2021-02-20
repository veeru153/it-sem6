from random import choice
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

activation = lambda x: -1 if x < 0 else 1

training_data = [ 
    (np.array([ 1, 1, 1]),  1),
    (np.array([ 1,-1, 1]), -1),
    (np.array([-1, 1, 1]), -1),
    (np.array([-1,-1, 1]), -1),
]

learning_rate = 0.2
training_steps = 100

W = np.random.rand(3) 
l1 = 1

for i in range(training_steps):
    x, y = choice(training_data)
    l1 = np.dot(W, x)

    y_pred = activation(l1)
    error = y - y_pred
    update = learning_rate * error * x
    W += update

print("Weights after Training: ")
print(W)
m = -1 * (W[0]/W[1])
c = -1 * (W[2]/W[1])

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.plot(0, "-")
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.scatter(-1, -1, c="r")
ax.scatter(-1, 1, c="r")
ax.scatter(1, -1, c="r")
ax.scatter(1, 1, c="g")
x_vals = np.arange(-3,3, 0.1)
ax.plot(x_vals, (m * x_vals + c), "-b")
plt.show()