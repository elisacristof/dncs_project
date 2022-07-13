#! /usr/bin/env python3

import tkinter as tk
import tkinter.font as font

def increase():
    if (int(lbl_value["text"])<6): 
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value + 1}"

def decrease():
    if (int(lbl_value["text"])>1):
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value - 1}"

def start():
    PcN = int(lbl_value["text"])
    
    print("You chose to create", PcN, "VMs") 
    btn_confirm["state"] = "disabled"
    win.destroy()
    
    print("Creating the VMs' scripts...")
    contenuto = "export DEBIAN_FRONTEND=noninteractive \n\n"
    num = 8

    for n in range(1, PcN+1):
        file = open("pc%d.sh" % n, 'w')
        file.write(contenuto)
        file.write("sudo ip addr add 192.168.0.%d/28 dev enp0s8 \n" % n)
        file.write("sudo ip link set dev enp0s8 up \n")
        file.close()
        
        file = open("router.sh", 'a')
        file.write("sudo ip addr add 192.168.1.%d/28 dev enp0s%d \n" % (n, num))  
        file.write("sudo ip link set dev enp0s%d up \n\n" % num)
        file.close()
        num += 1
        
    print("Updating the Vagrantfile...")
    f = open("Vagrantfile", "r")
    contents = f.readlines()
    f.close()
    
    contents.insert(19, "  (1..%d).each do |i|" % PcN) 

    f = open("Vagrantfile", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

    print("Now everything is ready!")
    print("You can modify the files or start the network with 'vagrant up'")


win = tk.Tk()
win.title("Choose the VMs' number")
win.geometry("330x200")
win.resizable(False,False)
win.configure(background="lightblue")

win.rowconfigure([0, 1], weight=1)
win.columnconfigure([0, 1, 2, 3], weight=1)


btn_decrease = tk.Button(master=win, text="-", bg="lightgreen", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
btn_decrease['font'] = font.Font(size=20)

lbl_value = tk.Label(master=win, text="1", bg="lightblue")
lbl_value.grid(row=0, column=1)
lbl_value['font'] = font.Font(size=20)

btn_increase = tk.Button(master=win, text="+", bg="lightgreen", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew", padx=4, pady=4)
btn_increase['font'] = font.Font(size=20)

btn_confirm = tk.Button(master=win, text="Okay", bg="yellow", command=start)
btn_confirm.grid(row=1, column=3, padx=4, pady=4)
btn_confirm['font'] = font.Font(size=12)


if __name__ == "__main__":
    win.mainloop()



