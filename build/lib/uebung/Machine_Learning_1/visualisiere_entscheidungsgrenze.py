import numpy as np
import matplotlib
matplotlib.use('Agg')  # Kein GUI nötig
import matplotlib.pyplot as plt

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


plt.savefig("plots/visualize_entscheidungsgrenze.png")
