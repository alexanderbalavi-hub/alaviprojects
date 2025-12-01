import numpy as np

def heaviside(x): # Schrittfunktion --> Aktivierungsfunktion
    if(x<0):
        return 0
    else:
        return 1

def sigmoid(x): # Sigmoidfunktion --> Aktivierungsfunnktion
    return 1 / (1 + np.exp(-x))   

# input: x1=cat, x2=shorthair, x3=grey
training_inputs = np.array([[0,1,1],
                            [1,1,1],
                            [1,0,1],
                            [1,1,0]])
training_outputs = np.array([[0,1,1,0]]) # expected outputs

lernrate = 0.1 # Learning rate, currently not used

bias=0.2 # Bias,used to shift activation function
#weights: w1,w2,w3
weights = np.array([[0.1,-0.4,0.3]]) # Initial weights, can be adjusted to tune the model besides bias

for i in range(len(training_inputs)):
    print("-----")
    output_expected = np.array(training_outputs[:,i], ndmin=2).T # expected output
    input = np.array(training_inputs[i], ndmin=2).T # input vector

    weighted_sum=np.dot(weights, input)+bias
    print('Wieghted sum: ', weighted_sum)

    output_heaviside=heaviside(weighted_sum)
    print('Heaviside activation function called.')
    print('Output Heaviside: ', output_heaviside)

    output_sigmoid=sigmoid(weighted_sum)
    print('Sigmoid activation function called.')
    print('Output Sigmoid: ', output_sigmoid)
    print("-----")

    output = heaviside(weighted_sum) # Choose activation function here
    error = output_expected - output # calculate error
    
    for n in range(0,len(weights[0,:])): # update weights from 0 to number of weights
        weights[:,n]=weights[:,n]+error*lernrate*training_inputs[i][n] # weight update rule 
        print('After ', weights[:,n]) # print updated weights

for i in range(len(training_inputs)):
    output_expected = np.array(training_outputs[:,i], ndmin=2).T # expected output
    output =heaviside(weighted_sum) # final output after training
    if output != output_expected:
        print("Error in training example: ", i) # print error message
        print("Output = ",output) # print actual output
        print("Expected output = ",output_expected) # print expected output