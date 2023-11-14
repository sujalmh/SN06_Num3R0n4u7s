# Need your Help

User `swapnilcrushes` wants to merge with his love interest. Can you help him do so by finding the flag?

## Solution:

1. Using a username search engine to find account related to `swapnilcrushes`.
2. A [github account](https://github.com/swapnilcrushes) is found.
3. Checking commits of the [repository](https://github.com/swapnilcrushes/this-is-my-repo), deleted files are discovered.
4. [this-is-my-repo/.bashrc](https://github.com/swapnilcrushes/this-is-my-repo/blob/72fb0854c987b7491b9523879e73cb88e7e5fc16/.bashrc) contains command `wget https://cantsee.sudooverride.tech/part3.sudo`, which gives an incomplete file.
5. Download part1.sudo and part2.sudo and combine all the three files to form a jpg file `cat part1.sudo part2.sudo part3.sudo > flag.jpg`.

The jpg file has the flag 
<p align="center">
 <img src="./Need your Help/flag.jpg" alt="flag.jpg" width="75%">
</p>

## Flag: sudo{am-i-a-normie?}

---

# The Secret

One of my friend Devansh told me about his town Maunath Bhanjan and a secret hidden in the toWn's history. He told that only the smartest geeks can uncover the secret of the town. One just needs to vIew the history of the history of the town to Know the hIdden secret.

## Solution:

1. Combining capital letters in the middle of the word gives WIKI.
2. [Maunath Bhanjan on Wikipedia](https://en.wikipedia.org/wiki/Mau,_Uttar_Pradesh) 
3. Check View history and opening the difference of edit from user DarmaniLink with the [previous revision](https://en.wikipedia.org/w/index.php?title=Mau,_Uttar_Pradesh&diff=prev&oldid=1183138872) gives the text: `secret : sudo{w1k1p3d1a_n3v3r_fa1l5_t0_h3lp}`
<p align="center">
 <img src="./The Secret/wiki.png" alt="wiki.png" width="75%">
</p>

## Flag: sudo{w1k1p3d1a_n3v3r_fa1l5_t0_h3lp}
