import numpy as np
from matplotlib import pyplot as plt

# make sure data files are available
np.loadtxt('data/noisy_data.txt')
np.loadtxt('data/regression_data.txt')

# make sure basic numpy functions work
x = np.arange(0, 2, 0.1)
y = x ** 2
z = 2 * x

# make sure basic plotting works
plt.plot(x, y)
plt.plot(x, z)
plt.show()