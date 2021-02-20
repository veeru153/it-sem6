from random import choice
import numpy as np
np.random.seed(1)

activation = lambda x: 0 if x < 0 else 1

training_data = [ 
    (np.array([0,0,1]), 0),
    (np.array([0,1,1]), 0),
    (np.array([1,0,1]), 0),
    (np.array([1,1,1]), 1),
]

# model parameters
learning_rate = 0.2 
training_steps = 100

# initialize weights 
W = np.random.rand(3) 

for i in range(training_steps):
    x, y = choice(training_data)
    
    l1 = np.dot(W, x)
    y_pred = activation(l1)

    error = y - y_pred
    update = learning_rate * error * x 
    W += update

# Output after training
print("Predictions after training")
for x, _ in training_data:
    y_pred = np.dot(x, W)
    print("{}:\t{}".format(x[:2], activation(y_pred)))