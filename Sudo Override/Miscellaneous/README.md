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
<p align="center">
 <img src="./Birthday Message/flag.png" alt="flag.png" width="75%">
</p>

### Flag: sudo{binary-it-is}

---

# It's all "@"

### File: confusing.txt

## Solution:

It looks like a QR code, but the QR format is wrong. Text editors are not able to render the characters correctly.

1. Open the file in terminal, the QR looks fine.
<p align="center">
 <img src="./It's all ''@''/terminal.png" alt="terminal.png" width="50%">
</p>

3. Editing confusing.txt according to the output in the terminal
4. Replacing "@" with "█"
<p align="center">
 <img src="./It's all ''@''/qr.png" alt="qr.png" width="50%">
</p>

6. Parsing QR gives the flag

### Flag: sudo{a5c11_roCk5}

