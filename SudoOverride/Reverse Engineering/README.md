# Iron Man

### File: iron

## Solution:

1. searching for `sudo` in iron using text editor gives the flag
<p align="center">
 <img src="./Iron Man/flag.png" alt="flag.png" width="75%">
</p>

## Flag: sudo{$0m3-Rus1y-F1@g}

---

# Just in Time

Sometimes, a little patience is all you need.

## Solution

1. The flag is printed if local_440 is greater or equal to condition, so changing it to if local_440 is lesser than or equal.
<p align="center">
 <img src="./Just In Time/assembly.png" alt="assembly.png" width="75%">
</p>

3. changing JLE to JGE in assembly will print the flag
<p align="center">
 <img src="./Just In Time/terminal.png" alt="terminal.png" width="75%">
</p>

## Flag: sudo{time.travel}

---

# Match the Following

### File: rev001

## Solution:

1. Analysing strings gives two strings which are relevant. One contains scrambled flag and another contains correct index of each character in hex.
<p align="center">
 <img src="./Match the Following/decompile.png" alt="decompile.png" width="75%">
</p>

3. Decoding using python
```python
flag_scrambled="au{u0veo}tiJp$tsm_r_ndt@"
flag_order="\x10\x02\x16\b\x03\f\x04\x0e\x0f\x14\x01\x12\r\a\x13\x11\x06\n\x18\x17\v\x05\x15\t"
flag_index=[]

#From Hex to Decimal
for h in flag_order:
   flag_index.append(ord(h)) 

flag=''

#Rearrange the flag by matching the index corresponding to each character
for i in flag_index:
   flag+=flag_scrambled[i-1]
print(flag)
```
## Flag: sudo{Ju$t_a_permvt@ti0n}
