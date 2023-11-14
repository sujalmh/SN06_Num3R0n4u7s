# QR Wordle

https://qr.sudooverride.tech/

## Solution:

It is not the optimal solution, but it was easier to get correct positions by getting green image in each cell. 

1. Download all the image parts.
2. Get the actual correct positions, by iterating until each image part has taken its correct position atleast once.
3. Merge the images sequentially considering the obtained actual correct positions.
4. Parsing the QR code gives the output:
<p align="center">
  <img src="./QR Wordle/merged_image.png" alt="Alt Text" width="50%">
</p>

```
We're no strangers to love
You know the rules and so do I (Do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
sudo{Ju5T_r0tat3_Cyclically}
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
```

### Flag: sudo{Ju5T_r0tat3_Cyclically}
