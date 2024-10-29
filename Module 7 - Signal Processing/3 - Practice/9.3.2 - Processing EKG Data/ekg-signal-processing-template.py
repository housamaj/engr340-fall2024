import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import filtfilt, butter

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = np.loadtxt(signal_filepath, skiprows=2,delimiter=',')
Elapsed_time_raw = signal[:,0]
V1_raw = signal[:,2]

plt.plot(Elapsed_time_raw,V1_raw)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("V5")
plt.show()

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

def low_pass_filter(data,order,cutoff_frequency,sampling_rate):
    b, a = butter(order, cutoff_frequency, btype='low', fs=sampling_rate)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

N = 6
F_c = 15
F_s = 250

filtered_signal = low_pass_filter(V1_raw,N,F_c,F_s)

plt.plot(Elapsed_time_raw,filtered_signal)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Low pass filter")
plt.show()

"""
Step 3: Pass data through weighted differentiator
"""

# MLII_diff = np.diff(MLII_raw)
V1_diff = np.diff(V1_raw, n=1,prepend=0)
plt.plot(Elapsed_time_raw,V1_diff)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Difference")
plt.show()

"""
Step 4: Square the results of the previous step
"""

V1_square = np.square(V1_diff)
plt.plot(Elapsed_time_raw,V1_square)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Square")
plt.show()

"""
Step 5: Pass a moving filter over your data
"""

V1_moving_average = np.convolve(V1_square, np.ones(10)/10, mode='same')
plt.plot(Elapsed_time_raw,V1_moving_average)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Moving average")
plt.show()