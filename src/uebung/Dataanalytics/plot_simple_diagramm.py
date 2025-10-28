import matplotlib
matplotlib.use('Agg')  # Kein GUI-Backend
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("output/plot.png")  # Speichert in Unterordner 'output'

