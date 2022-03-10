# CYBER STUDY


https://www.youtube.com/watch?v=bXCeFPNWjsM


## Rewerse shell and NetCat

When get target connect to your computer using netcat with certain definitions and your computer also run netcat as listener it provide shell access to target.


### Version control

```bash
sudo apt instal git
```

### Aliases

Edit file for aliases. It is run by .bashrc
~/.bash_aliases

```bash
alias hackwifi='besside-ngwlan0'
```

### Create non root user

```bash
sudo adduser pete
sudo usermod -aG pete 
```

### Multiwindow shell

```bash
sudo apt install tilix
tilix
```

### Install more tools. This is only example.

```bash
sudo apt update && sudo apt install kali-linux-rfid
```

Tor
Add tor into apt list

```bash
sudo echo 'deb https://deb.torproject.org/torproject.org stretch main
deb-src https://deb.torproject.org/torproject.org stretch main' > /etc/apt/sources.list.d/tor.list
```

Get tor key

```bash
sudo wget -O- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | sudo apt-key add -
```

Install using package manager

```bash
sudo apt update

sudo apt-get install tor deb.torproject.org-keyring
```
