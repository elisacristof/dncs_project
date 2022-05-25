export DEBIAN_FRONTEND=noninteractive

sudo sysctl -w net.ipv4.ip_forward=1

sudo ip addr add 192.168.1.1/28 dev enp0s8 
sudo ip link set dev enp0s8 up 

sudo ip addr add 192.168.1.2/28 dev enp0s8 
sudo ip link set dev enp0s9 up 

sudo ip addr add 192.168.1.3/28 dev enp0s8 
sudo ip link set dev enp0s10 up 

sudo ip addr add 192.168.1.4/28 dev enp0s8 
sudo ip link set dev enp0s11 up 

sudo ip addr add 192.168.1.5/28 dev enp0s8 
sudo ip link set dev enp0s12 up 

sudo ip addr add 192.168.1.6/28 dev enp0s8 
sudo ip link set dev enp0s13 up 

