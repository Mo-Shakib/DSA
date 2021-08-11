"""An IP address is divided into 4 sections where each section contains 1-3 
digits. An example of an IP address would be 192.168.10.3 . Now IP 
addresses have 2 parts; One is the network part while the other one is the 
host part. If the network part is 1, we get a special address from the 
given IP address where the 1st section will remain as it is and the rest of 
the 3 sections will become 0. If the network part is 2, we get a special 
address from the given IP address where the first 2 sections will remain as 
it is and the rest of the 2 sections will become 0. Same goes for other 
values of the network part. For simplicity we will consider the network 
part can be 1 or 2 or 3.
Lets see an example:

IP address: 192.168.10.30
If network part = 1 , then special address = 192.0.0.0
If network part = 2 , then special address = 192.168.0.0
If network bits = 3 , then special address = 192.168.10.0

All IP addresses starting like the special address will fall under the same 
special network. You will be given the value of the network part and a list 
of IP addresses as input. Your task will be to create a dictionary where 
the keys will be the unique special addresses and the corresponding values 
will be the list of IP addresses that fall under the same special network.

Input format: Value of network part<Space>List of IP addresses separated by """

ips = input()
address = ""
all_ips = {}
for ch in ips:
    if ch == ",":
        root = address[:8] + "0.0"
        if root in all_ips:
            all_ips[root].append(address)
        else:
            all_ips[root] = [address]
        address = ""
    else:
        address += ch
print(all_ips)