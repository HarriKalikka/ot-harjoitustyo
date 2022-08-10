# CYBER STUDY


## Kali Linux browse web as anonymous

Used for trying to hide original IP address. Original address need to find out from proxy server's logs and if chained it makes more difficult to investicate.

https://www.youtube.com/watch?v=2E7_2B-Vhas&t=331s

Find config.
```bash
$ locate proxychain
```
Could be here.
```bash
$ cat /etc/proxychains.conf
```

### Dynamic chain

Uncomment dynamic_chain and comment out strict_chain. Be sure that proxy_dns is also uncommented. Study what mean DNS leak.
```bash
$ sudo nano /etc/proxychains.conf
```

Add end of the file following line. This is for tor port 9050.
```bash
socks4  127.0.0.1 9050
socks5  127.0.0.1 9050
```
Where is proxyserver IP address and port.

Check if tor is running.
```bash
$ systemctl status tor
```

If not running thaen start tor.
```bash
$ sudo systemctl start tor
```

Use proxychain like following test
```bash
$ proxychains firefox www.duckduckgo.com
```

Then write into duckduckgo search "dns leak test". Should give proxyserver IP.
Try also get location or find location for IP address.
Write to search also "what is my ip address" to find other services.





