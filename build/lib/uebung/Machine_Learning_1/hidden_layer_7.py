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
epochs = 200
wih = 2 * np.random.random((3, 3)) - 1 # weights input to hidden, a 3x3 matrix with values from -1 to 1
who = 2 * np.random.random((1, 3)) - 1 # weights hidden to output, a 1x3 matrix with values from -1 to 1
np.random.seed(42)
print(wih)
print(who)

for e in range(0, epochs):
    for i in range(len(training_inputs)):
        output_expected = np.array(training_outputs[:, i], ndmin=2).T # transpose to make it a column vector
        input = np.array(training_inputs[i], ndmin=2).T # transpose to make it a column vector

        #Forward propagation    
        weighted_sum_hidden = np.dot(wih, input) + bias # weighted sum for hidden layer
        output_hidden = sigmoid(weighted_sum_hidden) # output of hidden layer

        weighted_sum_output =np.dot(who, output_hidden) # weighted sum for output layer
        output_output = sigmoid(weighted_sum_output) # output of output layer

        error = ((1 /2) * (np.power((output_expected - output_output), 2)))

        #Backpropagation
        #TODO: Output -> Hidden
        d_error_d_output_output = output_output - output_expected
        d_output_output_d_weightedsum_output = sigmoid_derivative(output_output)
        d_weightedsum_output_d_who = np.array(output_hidden, ndmin=2).T
        
        delta_who=np.dot(d_error_d_output_output * d_output_output_d_weightedsum_output, d_weightedsum_output_d_who)
        # TODO: Hidden -> Input
        d_error_d_output_hidden = np.dot(np.array(who, ndmin=2).T, d_error_d_output_output * d_output_output_d_weightedsum_output)
        d_output_hidden_d_weightedsum_hidden = sigmoid_derivative(output_hidden) # derivative of hidden layer output
        d_weightedsum_hidden_d_wih = np.array(input, ndmin=2).T # derivative of hidden layer weighted sum
        delta_wih = np.dot(d_error_d_output_hidden * d_output_hidden_d_weightedsum_hidden, d_weightedsum_hidden_d_wih)

        #TODO: Update weights
        who=who-L*delta_who
        wih=wih-L*delta_wih

print('Weights ih after epochs:\n', wih)
print('Weights ho after epochs:\n', who)

'''
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
'''