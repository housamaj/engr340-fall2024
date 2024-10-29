import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows
data = np.loadtxt(path, skiprows=2,delimiter=',')

Elapsed_time = data[:,0]
MLII = data[:,1]
V_1 = data[:,2]

# use matplot lib to generate a single

plt.plot(Elapsed_time, MLII)
plt.plot(Elapsed_time, V_1)
plt.show()