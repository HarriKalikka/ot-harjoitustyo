# CYBER STUDY


## Atom install to Kali linux


https://computingforgeeks.com/install-atom-text-editor-on-kali-linux/


Install Atom editor from website packagecloud.io.


### Installation

Update apt list.  
```bash
$ sudo apt update
```
Get wget and gpg.
```bash
$ sudo apt -y install wget gpg
```
Atom to apt list
```bash
$ sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
```
Check apt list.
```bash
$ cat /etc/apt/sources.list.d/atom.list
```
Get key.
```bash
$ curl -fsSL https://packagecloud.io/AtomEditor/atom/gpgkey | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/atom-keyring.gpg
```
Update apt list.  
```bash
$ sudo apt update
```
Get Atom.  
```bash
$ sudo apt install atom
```
What I done?
```bash
$ history
```

### Atom usage
