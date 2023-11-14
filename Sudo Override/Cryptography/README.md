# Weird Language

Augustus left behind an intriguing challenge inspired by his father, Julius. Despite the seemingly nonsensical nature of this task, it is exactly what Julius desired.

Animesh, our intrepid CTF moderator, has recently stumbled upon the secrets hidden by Augustus. However, he faces a conundrum - a locked crest that will only reveal its treasures when the correct flag is entered.

Animesh is willing to reward those who can decipher Augustus' cryptic message with valuable points. Are you up for the challenge?

flag : fhqb{rg_gh_oehgr}

## Solution

Rot-13/Caeser cipher

### flag: sudo{et_tu_brute}

---

# Locked Assignment

My friend pulled a prank, sending an encrypted PDF and a key. I need your help to decrypt it fast and submit my assignment. You should have a solid cryptography base for this.

### Files: key.png, Assignment.pdf

## Solution

1. key.png contains Text Description: ",]uL/?SHXlEcNmF70" in the metadata. 
2. Using https://gchq.github.io/CyberChef/, the key is encoded in Base85. 
3. Decoding ",]uL/?SHXlEcNmF70" gives "$uD0_0vErr1dE", which is the password for Assignment.pdf

### Flag: sudo{BaSe_85_EnCoDiNg}

