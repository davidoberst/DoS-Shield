
#--------DoS-Shield by davidoberst : https://github.com/davidoberst--------------
# ---------NOTICE: THIS TOOL DOES NOT STOP A DoS ATTACK------------------------.
# It simply detects network patterns such as multiple connections
# from the same IP, then blocks those IPs in the local machine’s
# firewall to mitigate the impact. USE IT AS A COMPLEMENTARY MEASURE,
# NOT AS A DEFINITIVE SOLUTION

from pyfiglet import figlet_format
from colorama import Fore,Style,Back
import time
from scapy.all import *
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

#--------------USER CHOICE-----------------
userChoice = input("--> ")
#---------------------TRAFIC SNIFFER FUNCTION-------------------
def traffficSniffer():

    #banner
    print(Style.BRIGHT +Fore.WHITE + figlet_format("TRAFFIC SNIFFER",font="cybermedium".rstrip())+ Style.RESET_ALL,end="") 
    print("please wait while DoS attack patterns are being searched...")
    print("-"*65)
    time.sleep(1)

    #logic
    check_user_iface = ('Get-NetAdapter -Physical | Select-Object Name -ExpandProperty Name')
    check_user_iface_result = subprocess.run(["powershell","-Command",check_user_iface],capture_output=True,text=True)

    #CHECK WHICH SERVICE ARE YOU USING
    if "Ethernet 3" in check_user_iface_result.stdout:
        ifaceResult = "Ethernet 3"
    elif "Ethernet 2" in check_user_iface_result.stdout:
        ifaceResult = "Ethernet 2"
    elif "Ethernet" in check_user_iface_result.stdout:
        ifaceResult = "Ethernet"
    # Wi-Fi / Wireless
    elif "Wi-Fi" in check_user_iface_result.stdout:
        ifaceResult = "Wi-Fi"
    elif "WiFi" in check_user_iface_result.stdout:
        ifaceResult = "WiFi"
    elif "WLAN" in check_user_iface_result.stdout:
        ifaceResult = "WLAN"
    elif "Wireless" in check_user_iface_result.stdout:
        ifaceResult = "Wireless"

    # Bluetooth PAN
    elif "Bluetooth" in check_user_iface_result.stdout:
        ifaceResult = "Bluetooth"

    # USB-LAN y docks
    elif "USB Ethernet" in check_user_iface_result.stdout:
        ifaceResult = "USB Ethernet"
    elif "USB 10/100/1000" in check_user_iface_result.stdout:
        ifaceResult = "USB 10/100/1000"
    elif "AX88179" in check_user_iface_result.stdout:
        ifaceResult = "AX88179"
    elif "DisplayLink" in check_user_iface_result.stdout:
        ifaceResult = "DisplayLink"

    # Fallback genérico
    else:
        ifaceResult = check_user_iface_result.stdout.splitlines()[0]

    #EXECUTE SCAPY SNIFFER WHITH IFACERESULT
    sniff(iface=ifaceResult, prn=lambda pkt: pkt.summary(), timeout=10)
    print("\n Process ended")

if userChoice == "1":
    time.sleep(1)
    traffficSniffer()
