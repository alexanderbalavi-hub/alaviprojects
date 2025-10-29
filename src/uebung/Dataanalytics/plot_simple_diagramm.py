import matplotlib
matplotlib.use('Agg')  # Kein GUI nötig
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("plots/plot2.png")

