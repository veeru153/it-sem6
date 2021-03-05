import numpy as np

threshold = 0
learningRate = 1

def activation(y_in):
    if y_in > threshold: return 1
    elif y_in < threshold: return -1
    else: return 0

trainingData = [
    (np.array([ 1, 1]),-1),
    (np.array([ 1,-1]),-1),
    (np.array([-1, 1]),-1),
    (np.array([-1,-1]), 1),
]

W = np.array([0,0])
b = 0

stop = False

while not stop:
    for j in range(len(trainingData)):
        x, t = trainingData[j]

        y_in = np.dot(W, x) + b
        y = activation(y_in)

        if y == t:
            stop = True
        else:
            W += learningRate * t * x
            b += learningRate * t
    
print(f"Weights after training: {W}")
print(f"Bias: {b}")