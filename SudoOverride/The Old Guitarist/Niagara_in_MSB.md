# Niagara in MSB

The image manages to slip past the LSB statistical check, but those funky visual quirks have us thinking there's more to it. The image ishere!

### File: Niagara_in_MSB.png

## Solution:

1. Using MSB to extract data using sigbits. `python3 sigBits.py -t=MSB Niagara_in_MSB.png`
2. grep to get flag from extracted data. `grep -o 'sudo{[^}]*}' outputSB.txt`

## Flag: sudo{the_Niagara_falls!!!} 