# "AUTOMATING THE DEPLOYMENT OF NETWORK SETUPS"
*The project consists of the development of a software that helps build a virtual network of PCs in an automated way using Vagrant.*
## DESIGN
I have designed the software so that the user can choose the number of PCs (from 1 to 6) in a star configuration, with a central router connecting the PCs together, in order to automatically generate the Vagrant scripts, which will activate the Virtual Machines and the router and connect them properly after launching the `vagrant up` command. If desired, the user can implement the routing by modifying the script files (.sh) after running the sotware.

![star](https://user-images.githubusercontent.com/89995099/170241546-8de5decb-9faa-49d7-8b0e-7799285b0b9f.jpg) *(configuration example)*

To implement my software I used Tkinter, a Python GUI (Graphical User Interface) package, and created a simple window with buttons where the user need to choose the VMs' number. 

![image](https://user-images.githubusercontent.com/89995099/178014871-dcc48f48-5cf8-472d-ad01-0ee27f511a33.png)

### User software requirements
- VirtualBox 
- Vagrant
- any Bash emulation to run Git from the command line

## IMPLEMENTATIONS
### GUI configuration
Firstly, I designed the visual interface as a simple **window** with two **buttons**, `+` and `-` (for the user to increase or decrease the PCs' number), and a `Okay` button to confirm the number chosen and give the input to automatically generate and update the scripts for Vagrant.
#### Window 
I chose to create a non resizable (with command `win.resizable(False,False)`) small (with command `win.geometry("330x200")`) window with a title (Choose the VMs' number) and a colored background (with command `win.configure(background="lightblue")`). 
#### Buttons
In order to create the buttons I used the widget class Button, available in the tkinter package with the command `tk.Button()` (I imported tkinter as tk). To each button I assigned the corresponding master (the same for all of them: the window), texts, color (green and yellow) and relative functions (`increase`, `decrease` and `start`). 
#### Functions
- `increase`: associated with the *"plus" button*, it increases the number of PCs by one when the user clicks on the button (the number cannot exceed 6);
- `decrease`: associated with the *"minus" button*, it decreases the number of PCs by one when the user clicks on the button (obviously the number cannot go below 1);
- `start`: associated with the "okay" button, this function reads the chosen PCs' number and initiates the process: it generates all the VMs scripts and updates the router's file and the Vagrantfile. 
#### General features
To make them more visible and pleasing to the eye, I decided to increment the font size to 20 of both the buttons, `+` and `-`, and the label. For the `Okay` button I chose a smaller size: 12. To do so I used the Font class constructor `*widgetname*['font'] = font.Font(size=*fontsize*)` (I imported tkinter.font module as font).
To specify the location of each button and label I called the geometry manager `.grid()` and passed the row and column indices.   
### Scripts commands 
Here there is a list of the commands used in the *shell scripts* (all preceded by `sudo` because every command has to be executed by the superuser):
- [**IP FORWARDING**] I enabled the IPv4 forwarding in the router with `sysctl -w net.ipv4.ip_forward=1`;
- [**IP**] I activated that interface with `ip link set dev [interface] up` and then I assigned an IP address to each interface, with the command `ip addr add [ip_address/netmask] dev [interface]`;

## EXECUTION
The user needs to download this repository to their PC. 
From the Bash software, the user must move to the corresponding folder and run the python file `gui.py`. The window will appear, from which the user can choose the desired pc number and confirm it. Then all the scripts are created and/or updated with the relative command lines.
Finally, the user can decide whether to edit the files, implementing routing if necessary, or run the `vagrant up` command to activate all Virtual Machines.  
