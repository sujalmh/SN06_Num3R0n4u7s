# Birthday Message

Darish decided to play a little birthday prank on Lalit, gifting him an audio file as a present. But Lalit's convinced there's a secret twist hidden in it. Can you be Lalit's partner-in-crime to unravel this audio enigma?

### File: audio.wav

## Solution

1. Opening audio file using audacity.
2. It is binary encoded, the highs being 1 and lows being 0.
3. Using python to get the binary string. 
4. Output: 
```
flag = "sudo{binary-it-is}"
print(flag)
```

### Flag: sudo{binary-it-is}