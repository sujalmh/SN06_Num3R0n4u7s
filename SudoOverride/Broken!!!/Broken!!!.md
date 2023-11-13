# Broken!!!

Here we have a decrytor, but its broken for some reason Decryptor.cpp. And here we have a key somewhere in this file : key.txt, but where to use it?

### File: Decryptor.cpp, key.txt

## Solution:
 
1. key.txt is a compressed file, which consists of a locked zip file containing random.pdf.
2. The code provided is used to convert hex to ascii, but it doesnt work since in the main function, "br0kEn" was hardcoded to be output. Corrected the output statement to print the variable asciiOutput instead of the string literal "brOkEn".
3. Using the first 32 characters of the key.txt file to get hex data (7423212449734E307454236546314047).
4. Hex data is used as input for Decryptor.cpp, which gives output (t#!$IsN0tT#eF1@G)
![output.png](./output.png)

6. Using `t#!$IsN0tT#eF1@G` as the password, to open random.pdf.
   
![random.pdf](./flag.png)

## Flag: sudo{So_it_wasn't_really_broken_huh}
