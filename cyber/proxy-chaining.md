# CYBER STUDY


## Kali Linux proxy chains config

Used for trying to hide original IP address. Original address need to find out from proxy server's logs and if chained it makes more difficult to investicate.

https://www.youtube.com/watch?v=qsA8zREbt6g

Find config.
```bash
$ locate proxychain
```
Could be here.
```bash
$ cat /etc/proxychains.conf
```

### Dynamic chain

Uncomment dynamic_chain and comment out strict_chain. Be sure that proxy_dns is also uncommented.  
```bash
$ sudo nano /etc/proxychains.conf
```
Add end of the file following line.
```bash
socks4 125.26.99.228 44052
```
Where is proxyserver IP address and port.

Use proxychain like following test
```bash
$ proxychains firefox google.com
```
Then write into google search "what's my ip address". Should give proxyserver IP.
Try also get location or find location for IP address.

Now it is more save to make port scanning example. Here target IP and ports.
```bash
$ proxychains nmap -sT -p 80,443 10.0.0.10
```
Add new line to config file.
Add end of the file following line.
```bash
http 3.236.52.219 8888
```
When try again then goes through 2 proxy.

You need find available proxyservers to use this. In google search write "free proxy server list" and find example spys.one to get list of free proxy servers. Then you need to try and test what works.




