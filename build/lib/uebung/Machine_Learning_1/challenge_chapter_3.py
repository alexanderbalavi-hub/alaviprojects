import numpy as np
import matplotlib
matplotlib.use('Agg')  # Kein GUI nötig
import matplotlib.pyplot as plt

learning_rate=0.8

#array with radius, sweetness, label (0== raspberry, 1==lemon)
fruit_array=np.array([(0.5,3,0),(4.5,0.5,1),(1.2,4.5,0),
                          (0.9,3.6,0),(4,0.97,1),(4.3,0.88,1),
                          (2.3,4.2,0),(3.5,0.2,1),(2,4.8,0),
                          (3,0.9,1),(2.8,3.4,0),(3.8,0.7,1)])
                       
max_x=5
max_y=5
#set the plot markers, axis ranges and labels
plt.rcParams['lines.markersize'] = 8
plt.rcParams['lines.linewidth'] = 2
plt.axis([0, max_x, 0, max_y])
plt.xlabel('radius')
plt.ylabel("sweetness")
plt.grid()

#10 evenlyspace points between 0 and 5
x=np.linspace(0,5,10)

#TODO: compute first decision boundary (i.e. determine b, m and y)

#TODO: update m and y with each new data point


for data_point in fruit_array:
    if data_point[2]==0:
        plt.plot(data_point[0], data_point[1], 'ro')
    else:
        plt.plot(data_point[0], data_point[1], 'yo')
      

plt.savefig("plots/Machine_Learning_1/plot_challenge_chapter_3.png")