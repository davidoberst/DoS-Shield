
#--------DoS-Shield by davidoberst : https://github.com/davidoberst--------------
# ---------NOTICE: THIS TOOL DOES NOT STOP A DoS ATTACK------------------------.
# It simply detects network patterns such as multiple connections
# from the same IP, then blocks those IPs in the local machine’s
# firewall to mitigate the impact. USE IT AS A COMPLEMENTARY MEASURE,
# NOT AS A DEFINITIVE SOLUTION

from pyfiglet import figlet_format
from colorama import Fore,Style,Back
import time
import subprocess

#---------------------------------BANNER AND ADVISES-------------------------------------------------------------
print("");print("");print("");
banner = Style.BRIGHT +Fore.WHITE + figlet_format("   DoS Shield",font="cybermedium".rstrip())+ Style.RESET_ALL
print(banner, end="");print(Fore.WHITE +  "       v1 | by davidoberst | https://github.com/davidoberst " + Style.RESET_ALL + Style.RESET_ALL)
print("-"*65)
print(" " * 8 + Back.RED + "NOTICE: THIS TOOL DOES NOT STOP A DoS ATTACK." + Style.RESET_ALL, end="")
print(Style.BRIGHT + Fore.YELLOW +"""
 It simply detects network patterns such as multiple connections
 from the same IP, then blocks those IPs in the local machine’s
 firewall to mitigate the impact. USE IT AS A COMPLEMENTARY MEASURE
 NOT AS A DEFINITIVE SOLUTION
"""+Style.RESET_ALL,end="")
print("-"*65)
#choose options
print(Fore.WHITE + "[1] Trafic Sniffer")
print(Fore.WHITE + "[2] Block IP (Manual)")
print(Fore.WHITE + "[3] Blocked IP Dashboard")
print(Fore.WHITE + "[4] Help (See what each choice does)")
print(Fore.WHITE + "[5] Exit")
print("-" * 65)
 
userChoice = input("--> ")

#---------------------TRAFIC SNIFFER FUNCTION-------------------
def traffficSniffer():
   print(Style.BRIGHT +Fore.WHITE + figlet_format("TRAFFIC SNIFFER",font="cybermedium".rstrip())+ Style.RESET_ALL,end="") 
   print("-"*65)
 
if userChoice == "1":
    time.sleep(1)
    traffficSniffer()








