# Match The Following

### File: rev001

## Solution:

1. Analysing strings gives two strings which are relevant. One contains scrambled flag and another contains correct index of each character in hex.
![disassemble](./decompile.png)

2. Decoding using python
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
