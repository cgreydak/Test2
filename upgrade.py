import os
os.system ("apt update && apt list upgradable")
os.system ("sleep 5")
os.system ("apt upgrade && exit")
os.system ("sudo -k")
print("")
print("")
print("the end of the upgrade program")
print("")
print("")
