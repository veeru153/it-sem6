import numpy as np
np.random.seed(1)

activation = lambda x: -1 if x < 0 else 1
classify = lambda x: "2 (O)" if x == -1 else "1 (C)"

C = np.ravel([
    (np.array([ 1, 1, 1])),
    (np.array([ 1,-1,-1])),
    (np.array([ 1, 1, 1]))
])

O = np.ravel([
    (np.array([ 1, 1, 1])),
    (np.array([ 1,-1, 1])),
    (np.array([ 1, 1, 1]))
])

training_data = [
    (np.append(C, 1), 1),
    (np.append(O, 1),-1)
]

# model parameters
learning_rate = 0.2 
training_steps = 100

# initialize weights 
W = np.random.rand(10)

for data in training_data:
    x, y = data
    for i in range(training_steps):
        update = learning_rate * y * x 
        W += update


def predict(W, dataset):
    y_pred = np.dot(np.append(dataset, 1), W)
    y = activation(y_pred)
    print(f"Class: {classify(y)}")

# Testing Data Sets
testSets = [
    np.ravel([
        (np.array([ 1, 1,-1])),
        (np.array([ 1,-1,-1])),
        (np.array([ 1, 1, 1]))
    ]),
    np.ravel([
        (np.array([ 1, 1,-1])),
        (np.array([ 1,-1, 1])),
        (np.array([ 1, 1, 1]))
    ])
]

for index, testSet in enumerate(testSets, start=1):
    print(f"Set {index} - ", end="")
    predict(W, testSet)
