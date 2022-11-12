# python code by Mubarak Aliyu Danjuma
import os

network_range = input("Please enter network address in 'x.x.x.' format \n")

range_1 = input("Please enter the first range: \n")
range_2 = input("Please enter the second range: \n")

print("Initializing IP Sweep...")

with open("foundIP.txt", "a") as myfile:
    myfile.write("Found IPS: \n")

for ip in range(int(range_1), int(range_2)+1):
    address = network_range + str(ip)
    res = os.system("ping -c 1 -w 1 " + address + ">/dev/null")
    if res == 0:
        with open("foundIP.txt", "a") as myfile:
            myfile.write(address + "\n")

print("IP Sweep is done. Check the txt file!")