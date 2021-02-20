from random import choice
import numpy as np
np.random.seed(1)

activation = lambda x: -1 if x < 0 else 1

training_data = [ 
    (np.array([-1,-1, 1]),  1),
    (np.array([-1, 1, 1]),  1),
    (np.array([ 1,-1, 1]),  1),
    (np.array([ 1, 1, 1]), -1),
]

# model parameters
learning_rate = 0.2 
training_steps = 100

# initialize weights 
W = np.random.rand(3) 

for i in range(training_steps):
    
    x, y = choice(training_data)
    update = learning_rate * y * x 
    W += update

print("Weights after Training: ")
print(W)