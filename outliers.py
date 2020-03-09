# Setup
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('dark_background')

# Data import/creation
data = np.loadtxt('data/noisy_data.txt')
x = np.arange(data.size)

# Data analysis
mu = np.mean(data)
std = np.std(data)

# Data manipulation
outliers = np.abs(data - mu) > 3 * std
good_data = np.logical_not(outliers)

# Data visualization
plt.title('Noisy Data')
plt.scatter(x[outliers], data[outliers], marker='.', color='r')
plt.scatter(x[good_data], data[good_data], marker='.', color='w')
plt.hlines([mu], 0, data.size, colors='m', linewidth=3)
plt.hlines([mu + std, mu - std, mu + 3 * std, mu - 3 * std], 0, data.size, 'b', linestyles='dashed')
plt.show()