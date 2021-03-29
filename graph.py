import numpy as np
import matplotlib.pyplot as plt


num_examples = 50
X = np.array([np.linspace(-2, 4, num_examples), np.linspace(-6, 6, num_examples)])
plt.figure(figsize = (5, 5))
plt.scatter(X[0], X[1])
plt.show()
