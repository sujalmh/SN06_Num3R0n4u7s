# Locked Assignment

My friend pulled a prank, sending an encrypted PDF and a key. I need your help to decrypt it fast and submit my assignment. You should have a solid cryptography base for this.

### Files: key.png, Assignment.pdf

## Solution

1. key.png contains Description: ",]uL/?SHXlEcNmF70" in the metadata. 
2. Using https://gchq.github.io/CyberChef/, the key is encoded in Base85. 
3. Decoding ",]uL/?SHXlEcNmF70" gives "$uD0_0vErr1dE", which is the password for Assignment.pdf

### flag: sudo{BaSe_85_EnCoDiNg}