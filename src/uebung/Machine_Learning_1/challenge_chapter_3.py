import numpy as np
import matplotlib
matplotlib.use('Agg')  # Kein GUI nötig
import matplotlib.pyplot as plt


learning_rate=0.8

def update_m(m,b,new_data_point,label):
    if label==0:
        y_target=new_data_point[1]-1
    else:
        y_target=new_data_point[1]+1
    y_is=new_data_point[0]*m+b
    
    #error 
    error=(y_target-y_is)
    
    delta_m=(error/new_data_point[0])*learning_rate
    m_new=m+delta_m
    y_new=x*m_new+b

    return y_new

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

#compute first decision boundary (i.e. determine b, m and y)
b=0
if fruit_array[0][2]==0:
    #raspberry point underneath
    m=(fruit_array[0][1]-1-b)/fruit_array[0][0]
else:
    #lemon point above
    m=(fruit_array[0][1]+1-b)/fruit_array[0][0]
y_new=m*x+b

#update m and y with each new data point
for data_point in fruit_array:
    if data_point[2]==0:
        plt.plot(data_point[0], data_point[1], 'ro')
    else:
        plt.plot(data_point[0], data_point[1], 'yo')

    y_new=update_m(m,b,data_point[0:2],data_point[2])
    plt.plot(x, y_new, '-b', linestyle='--')
    
plt.plot(x, y_new, '-g', linestyle='--')     

plt.savefig("plots/Machine_Learning_1/plot_decision_boundary_2.png")