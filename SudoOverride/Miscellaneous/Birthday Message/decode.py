from scipy.io import wavfile
import numpy as np

#convert bits to ascii
def bits2a(b):
     return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))
 
# Load the WAV file
input_file = 'audio.wav'
output_file = 'binary_output.wav'

# Read the WAV file
sample_rate, audio_data = wavfile.read(input_file)

# Apply Binarization
threshold = 0  # Adjust this value based on your audio characteristics
binary_audio = list((audio_data > threshold).astype(np.int16))

# Save the binary audio to a new WAV file
bin=[str(i) for i in binary_audio]
out=''.join(bin)
print(bits2a(out))
