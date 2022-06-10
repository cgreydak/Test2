import os
print("This is Python script to upgrade my Linux Devnet Desktop")
os.system ("apt update && apt list --upgradable")
print("*************************************")
print("Check the list of upgradable packages")
print("*************************************")
os.system ("sleep 20")
print("type y if you want to continue or type n if you want to exit")
a=input()
while a=="n":
	print()
	print("********************************")
	print("Linux packages were not upgraded")
	print("********************************")
	a=("donotupgrade")
while a=="y": 
	os.system ("apt upgrade && exit")
	os.system ("sudo -k")
	a="Stop"
	print()
	print("************************")
	print("The upgrade is completed")
	print("************************")