import os
print("This is Python script to upgrade my Linux Devnet Desktop")
os.system ("apt update && apt list --upgradable")
print()
print("*************************************")
print("Check the list of upgradable packages")
print("and decide if you want upgrade or not")
print("*************************************")
print()
print()
#os.system ("sleep 3")
print("type y if you want to continue or type n if you want to exit")
a=input()
while a!="y" and a!="n":
	try:
		print()
		print("************************************************************")
		print("Type y if you want to continue or type n if you want to exit")
		print("or type Ctl+C to exit the program")
		print("************************************************************")
		print()
		a=input()
	except ValueError:
		a=input()
while a=="n":
	print()
	print("********************************")
	print("Linux packages were not upgraded")
	print("********************************")
	a="stop"
while a=="y": 
	os.system ("apt upgrade && exit")
	os.system ("sudo -k")
	print()
	print("************************")
	print("The upgrade is completed")
	print("************************")
	a="stop"



	
	
			
