import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io import wavfile 

sampling_freq, signal = wavfile.read('random_sound.wav') 

print('Signal shape:', signal.shape) 
print('Datatype:', signal.dtype) 
print('Signal duration:', round(signal.shape[0] / float(sampling_freq), 2), 'seconds')

signal = signal / (2 ** 15)
size = 50
signal = signal[:size] 
time_axis = np.linspace(0, 1000 * size / sampling_freq, size)

plt.plot(time_axis, signal, color='black') 
plt.xlabel('Time (milliseconds)') 
plt.ylabel('Amplitude') 
plt.title('Input audio signal') 
plt.show()