# CYBER STUDY


## Google hacking


https://www.youtube.com/watch?v=hrVa_dhD-iA


Using google for gathering information.


### google search operators

Site operator to define the site where search.  
```bash
<keyword> site:<domain>
```
Inurl find text used in url.
```bash
site:<domain> inurl:<keyword>
site:starbucks.com inurl:admin
```
Intext 
```bash
site:<domain> intext:<keyword>
```
Intitle
```bash
site:<domain> intitle:<keyword>
site:starbucks.com inurl:login
```
Filetype
```bash
site:<domain> filetype:<type>
site:starbucks.com filetype:pdf
```

### google hacking database

Just search this in google search.
Can find example
```bash
intitle:"WEBCAM 7" -inurl: /admin.html 
```


### Kali linux harvester



```bash
$ theHarvester -d starbucks.com -b google
$ theHarvester -d starbucks.com -b netcraft
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




