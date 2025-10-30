import numpy as np
import matplotlib
matplotlib.use('Agg')  # Kein GUI nötig
import matplotlib.pyplot as plt

learning_rate=1
# set global learning rate. A high learning rate can lead to overshooting the optimal solution, 
# while a low learning rate can make the training process very slow. 
# Recommended to start with a small value like 0.01 or 0.001 and adjust as needed.

def update_m(m,b,x,new_data_point,label):
    if label==0: #dog
        y_target=new_data_point[1]-1 #set target value slightly below the actual value
        print(y_target)
    else: #cat
        y_target=new_data_point[1]+1 #set target value slightly above the actual value
    y_is=new_data_point[0]*m+b

    #error
    error=(y_target - y_is)

    delta_m=(error/new_data_point[0])*learning_rate
    print(delta_m)
    m_new=m+delta_m
    y_new=x*m_new+b
    plt.plot(x,y_new,'-b',linestyle='-.')       

# Generate synthetic data
# Dog domestication dataset
dogs=np.array([(0.9,0.88,0.99),(57,38,23)]) #dog domesitcation factor and dog size
# Cat domestication dataset
cats=np.array([(0.1,0.2,0.4),(8,12,22)]) #cat domestication factor and cat size

#separate x and y axis values of the plot
dogs_domestication_factor=dogs[0,:] #
dogs_size=dogs[1,:] #
cats_domestication_factor=cats[0,:] #
cats_size=cats[1,:] #

#set the plot markes, axis ranges and labels
plt.rcParams['lines.markersize'] = 10
plt.rcParams['lines.linewidth'] = 2
plt.axis([0, 1, 0, 60])
plt.xlabel('Domestication Factor')
plt.ylabel('Size in cm')
plt.grid() 

#plot size against domestication factor for dogs and cats
plt.plot(dogs_domestication_factor, dogs_size, 'ro', label='Dogs')
plt.plot(cats_domestication_factor, cats_size, 'bo', label='Cats')

#plot decision boundary
x = np.linspace(0, 1, 10) # x values for decision boundary line
m =-80
b = 60
y = m*x +b # y values for decision boundary line
plt.plot(x, y, '-g', label='Decision Boundary', linestyle='--') #green decision boundary

#add new datapoint
maine_coon=np.array([(0.4),(35)])
plt.plot(maine_coon[0],maine_coon[1],'ms')

update_m(m,b,x,maine_coon,1)

#add new dog datapoint
new_dog=np.array([(0.75),(30)])
plt.plot(new_dog[0], new_dog[1],'mo')

update_m(m,b,x,new_dog,0)

#calculate error
current = maine_coon[0]*m+b
error=(maine_coon[1]+1 - current)

#update m
m=m+(error/maine_coon[0])
y_new=x*m+b
plt.plot(x,y_new,'c',linestyle='-.') #cyan decision boundary

plt.savefig("plots/Machine_Learning_1/plot_decision_boundary_1.png")
