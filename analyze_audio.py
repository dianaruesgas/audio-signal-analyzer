import numpy  #for math and arrays
import matplotlib.pyplot as plt #to draw graphs
from scipy.io import wavfile #in order to load .wav files


# Load the audio file
#wavfile lets the user work with .wav files
#the function read read the content of audio1
#the integer rate tells hown many audio samples were taken per second (in Hz)
# sound is a NumPy array (list of numbers). Here, every number is one sample of audio; 1D for mono, 2D for stereo 
rate, sound = wavfile.read("audio1.wav")

# Now we check if the audio has 2 channels (stereo), use only one
#ndim is used to tell the number of dimensionsof the array (here 1 or 2)
if sound.ndim == 2: #if the audio is stereo...
    sound = sound[:, 0] #we keep the left channel since our goal is to get a 1D signal

# A time axis for plotting is created
length = len(sound)
times = numpy.arange(length) / rate

# Plot the waveform (time domain)
plt.plot(times, sound)
plt.title("Sound Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# Perform FFT to get frequency information
fft_result = numpy.fft.fft(sound)
magnitudes = numpy.abs(fft_result)
frequencies = numpy.fft.fftfreq(length, 1 / rate)

# Only show positive frequencies
half = length // 2
plt.plot(frequencies[:half], magnitudes[:half])
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

