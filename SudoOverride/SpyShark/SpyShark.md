# SpyShark

I have discovered a suspicious pcap file in my trash folder. I suspect that it is a log dump of one of my usb devices and might also contain some confidential data. To successfully complete this challenge, you'll need to employ your forensic skills and unravel the secrets hidden in the pcap file.

Hint: The USB Device turns out to be a Keyboard

### File: keylogger_dump.pcap

## Solution:

1. tshark to strip out only the keyscans `tshark -r ./keylogger_dump.pcap -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > keystrokes.txt`
2. Use the tool [ctf-usb-keyboard-parser](https://github.com/carlospolop-forks/ctf-usb-keyboard-parser) to get what was written in the communication

# Flag: sudo{ShArKs_SPYing_ME}