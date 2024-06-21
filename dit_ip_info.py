import requests
import sys
import subprocess
import os
import socket
import nmap
from rich import print

sys.tracebacklimit = 0

def info(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        
        data = {
            "IP": response.get("query"),
            "Country": response.get("country"),
            "Region": response.get("regionName"),
            "City": response.get("city"),
            "Zip-code": response.get("zip"),
            "Lat": response.get("lat"),
            "Long": response.get("lon"),
            "Timezone": response.get("timezone"),
            "Provider": response.get("isp"),
            "Organization": response.get("org"),
            "status": response.get("status"),
            "org": response.get("org"),
        }

        for k, e in data.items():
            print(f"[bold cyan]{k}: [bold yellow]{e}")
        print("")

    except Exception as e:
        print(f"[bold red]An '{e}' error occurred")

def ping(ip):
    try:
        # Use 'ping -c 4' for Unix/Linux/Mac and 'ping -n 4' for Windows
        param = '-n' if sys.platform.startswith('win') else '-c'
        command = ['ping', param, '4', ip]
        response = subprocess.run(command, capture_output=True, text=True)
        print(f"[bold cyan]{response.stdout}[/bold cyan]")
    except Exception as e:
        print(f"[bold red]An '{e}' error occurred while pinging {ip}")

def get_website_ip(website):
    try:
        ip = socket.gethostbyname(website)
        print(f"[bold cyan]The IP address of [bold yellow]{website}[/bold yellow] is [bold green]{ip}[/bold green]")
    except Exception as e:
        print(f"[bold red]An '{e}' error occurred while getting the IP of {website}")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"[bold red]An '{e}' error occurred while getting the local IP address")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def nmap_scan(ip, arguments=''):
    try:
        nm = nmap.PortScanner()
        nm.scan(ip, arguments=arguments)
        for host in nm.all_hosts():
            print(f"[bold cyan]Host : {host} ({nm[host].hostname()})")
            print("[bold yellow]State : {0}".format(nm[host].state()))
            for proto in nm[host].all_protocols():
                print("----------")
                print(f"[bold yellow]Protocol : {proto}")
                lport = nm[host][proto].keys()
                for port in lport:
                    print(f"[bold yellow]Port : {port} \t State : {nm[host][proto][port]['state']}")
            if 'osmatch' in nm[host]:
                print("[bold cyan]OS matches:")
                for osmatch in nm[host]['osmatch']:
                    print(f"[bold cyan]Name: {osmatch['name']} \tAccuracy: {osmatch['accuracy']}")
            if 'osclass' in nm[host]:
                print("[bold cyan]OS details:")
                for osclass in nm[host]['osclass']:
                    print(f"[bold cyan]Vendor: {osclass['vendor']} \tOS Family: {osclass['osfamily']} \tOS Gen: {osclass['osgen']}")
            print("")

    except Exception as e:
        print(f"[bold red]An '{e}' error occurred during the Nmap scan")

def web_app_enum(ip):
    try:
        # You can replace this with your own script for web application enumeration
        print("[bold cyan]Performing web application enumeration...")
        subprocess.run(['./web_app_enum_script.sh', ip], capture_output=True, text=True)
    except Exception as e:
        print(f"[bold red]An '{e}' error occurred during web application enumeration")

def main():
    clear_screen()  # Automatically clear the screen when the tool is run
    ascii_art = '''
    ██╗██████╗       ██╗███╗   ██╗███████╗ ██████╗ 
    ██║██╔══██╗      ██║████╗  ██║██╔════╝██╔═══██╗
    ██║██████╔╝█████╗██║██╔██╗ ██║█████╗  ██║   ██║
    ██║██╔═══╝ ╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
    ██║██║           ██║██║ ╚████║██║     ╚██████╔╝
    ╚═╝╚═╝           ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                   
    '''
    while True:
        print(f"[bold yellow]{ascii_art}[/bold yellow]")
        print("[bold cyan]1 - Your [yellow]IP address[/yellow];\n2 - Info about [yellow]any IP address[/yellow];\n3 - Info about [yellow] Developer[/yellow];\n4 - [yellow]Ping an IP address[/yellow];\n5 - Get the [yellow]IP address of a website[/yellow];\n6 - Get your [yellow]Local IP address[/yellow];\n7 - [yellow]Nmap Scan[/yellow];\n8 - [yellow]Web Application Enumeration[/yellow]\n")
        choice = input(">>> ")
        if choice.lower() in ['cls', 'clear']:
            clear_screen()
        elif choice.lower() == 'exit':
            print("Exiting the program...")
            break  # Exit the while loop and end the program
        else:
            try:
                choice = int(choice)
            except:
                print("[bold red]Type 1, 2, 3, 4, 5, 6, 7, 8, or 'exit'!")
            else:
                if choice == 1:
                    url = "https://icanhazip.com/"
                    response = requests.get(url).text.strip()
                    print(f"[bold green]Your IP is [bold yellow]{response}")
                elif choice == 3:
                    print("Hi, This tool is created in Python and developed by Dit-Developers")
                elif choice == 2:
                    print("[cyan]Enter an IP that will be checked")
                    try:
                        ip = input("IP: ")
                        info(ip)
                    except Exception as e:
                        print(f"[bold red][ERROR] {e}")
                elif choice == 4:
                    print("[cyan]Enter an IP to ping")
                    try:
                        ip = input("IP: ")
                        ping(ip)
                    except Exception as e:
                        print(f"[bold red][ERROR] {e}")
                elif choice == 5:
                    print("[cyan]Enter a website URL")
                    try:
                        website = input("Website: ")
                        get_website_ip(website)
                    except Exception as e:
                        print(f"[bold red][ERROR] {e}")
                elif choice == 6:
                    local_ip = get_local_ip()
                    if local_ip:
                        print(f"[bold cyan]Your Local IP address is [bold yellow]{local_ip}")
                elif choice == 7:
                    print("[cyan]Enter an IP for Nmap scan")
                    try:
                        ip = input("IP: ")
                        nmap_scan(ip)
                    except Exception as e:
                        print(f"[bold red][ERROR] {e}")
                elif choice == 8:
                    print("[cyan]Enter an IP for web application enumeration")
                    try:
                        ip = input("IP: ")
                        web_app_enum(ip)
                    except Exception as e:
                        print(f"[bold red][ERROR] {e}")

if __name__ == "__main__":
    main()

# This code is licensed under the MIT License.
# All rights reserved by MSU and DIT Developers.
# For more details, see the LICENSE file.
    # <!-- ©Dit-Developers -->
