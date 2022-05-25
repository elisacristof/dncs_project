# "AUTOMATING THE DEPLOYMENT OF NETWORK SETUPS"
The project is to develop software to build a virtual network of PCs in an automated way using Vagrant.
## DESIGN
I have designed the software so that the user can choose the number of PCs (from 1 to 6) in a star configuration, with a central router connecting the PCs together, and automatically generate Vagrant scripts, which will activate the Virtual Machines and the router and connect them properly after launching the `vagrant up` command.

![star](https://user-images.githubusercontent.com/89995099/170241546-8de5decb-9faa-49d7-8b0e-7799285b0b9f.jpg) *(example of configuration)*

To implement my software I used Tkinter, a Python GUI (Graphical User Interface) package, and created a simple window with buttons where the user choose the VMs' number.

![window](https://user-images.githubusercontent.com/89995099/170240351-e746dead-76fe-4ca5-9e28-224fdc71b762.png)

### User requirements
- VirtualBox 
- Vagrant
- 

## IMPLEMENTATIONS
### Configuring the GUI

### Commands 
Here there is a list of the commands used in the *.sh scripts* (all preceded by `sudo` because every command has to be executed by the superuser):
- [**IP FORWARDING**] I enabled the IPv4 forwarding in the router with `sysctl -w net.ipv4.ip_forward=1`;
- [**IP**] I assigned an IP address to each interface, with the command `ip addr add [ip_address/netmask] dev [interface]` and then I activated that interface with `ip link set dev [interface] up`;
