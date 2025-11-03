import numpy as np

def sigmoid(x): #activation function
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x)) #derivative of sigmoid function


#input: x1=cat, x2=shorthair, x3=grey
training_inputs = np.array([[0, 1, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [1, 1, 0]])
training_outputs = np.array([[0, 1, 1, 0]])

#inputs within activation function range
training_inputs = training_inputs * 0.98 + 0.01

# outputs withing activation function range
training_outputs = training_outputs * 0.98 + 0.01

bias = 0.2
L = 0.1
epochs = 2000

np.random.seed(42)
weights = 2 * np.random.random((1, 3)) - 1
print(weights)

for e in range(0, epochs):
    for i in range(len(training_inputs)):
        print("-------")
        output_expected = np.array(training_outputs[:, i], ndmin=2).T
        input = np.array(training_inputs[i], ndmin=2).T

        #Forward propagation    
        weighted_sum = np.dot(weights, input) + bias
        output = sigmoid(weighted_sum)

        error = ((1 /2) * (np.power((output_expected - output), 2)))

        #Backpropagation
        d_error_d_output_output = output - output_expected
        d_output_output_d_weighted_sum = sigmoid_derivative(output)
        d_weightedsum_d_weights = np.array(input, ndmin=2).T
        
        delta_weights=np.dot(d_error_d_output_output * d_output_output_d_weighted_sum, d_weightedsum_d_weights)
        weights=weights-L*delta_weights

print("-------")
print('Weights after epochs:\n', weights)
correct = 0
for i in range(len(training_inputs)):
    output_expected = np.array(training_outputs[:, i], ndmin=2).T
    input = np.array(training_inputs[i], ndmin=2).T

    weighted_sum = np.dot(weights, input) + bias
    output_output = sigmoid(weighted_sum)
    output = 0.01
    if (output_output >= 0.5):
        output = 0.99
    if output != output_expected:
        print('Error in training example ', i)
    else:
        correct +=1
    print('Output Neuronal network', output_output)
    print('Expected output', output_expected)

print('Accuracy:', correct/len(training_inputs))
