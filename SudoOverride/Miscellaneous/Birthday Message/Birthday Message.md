# Birthday Message

Darish decided to play a little birthday prank on Lalit, gifting him an audio file as a present. But Lalit's convinced there's a secret twist hidden in it. Can you be Lalit's partner-in-crime to unravel this audio enigma?

### File: audio.wav

## Solution

1. Opening audio file using audacity.
2. It is binary encoded, the highs being 1 and lows being 0.
3. Using python to get the binary string.
```python
from scipy.io import wavfile
import numpy as np

#convert bits to ascii
def b2a(b):
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
print(b2a(out))
```
Output: 
```
flag = "sudo{binary-it-is}"
print(flag)
```
![Flag](./flag.png)

### Flag: sudo{binary-it-is}