import os
import subprocess
import re

class WhoisTool:
    def __init__(self):
        self.whoisPrompt = "Enter Domain or IP for Whois Lookup (or type 'exit' to quit): "
        self.whoisLogo = """
        ====================================
        |         Whois Lookup Tool        |
        ====================================
        """
        if not self.installed():
            print("[!] Whois is not installed.")
            exit(1)
        self.run()

    def installed(self):
        return os.path.isfile("/usr/bin/whois") or os.path.isfile("/usr/local/bin/whois")

    def run(self):
        while True:
            self.clear_screen()
            print(self.whoisLogo)
            target = input(self.whoisPrompt).strip()
            if target.lower() == 'exit':
                print("[*] Exiting Whois Lookup Tool...")
                break
            if not self.is_valid_domain_or_ip(target):
                print("[!] Invalid domain or IP address. Please try again.")
                input("Press Enter to continue...")
                continue
            result = self.lookup(target)
            print("\n" + result)
            choice = input("\nDo you want to perform another Whois lookup? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("[*] Exiting Whois Lookup Tool...")
                break

    def is_valid_domain_or_ip(self, target):
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9]'  
            r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)'  
            r'+[a-zA-Z]{2,6}$'
        )
        ip_regex = re.compile(
            r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'  
        )
        return domain_regex.match(target) or ip_regex.match(target)

    def lookup(self, target):
        self.clear_screen()
        print(f"Performing Whois lookup for: {target}\n")
        try:
            result = subprocess.run(["whois", target], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"[!] Error performing Whois lookup: {e}")
            return f"Error: {e}"

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


class DigTool:
    def __init__(self):
        self.digPrompt = "Enter Domain for DNS Lookup (or type 'exit' to quit): "
        self.digLogo = """
        ====================================
        |          Dig Lookup Tool         |
        ====================================
        """
        if not self.installed():
            print("[!] Dig is not installed.")
            exit(1)
        self.run()

    def installed(self):
        return os.path.isfile("/usr/bin/dig") or os.path.isfile("/usr/local/bin/dig")

    def run(self):
        while True:
            self.clear_screen()
            print(self.digLogo)
            domain = input(self.digPrompt).strip()
            if domain.lower() == 'exit':
                print("[*] Exiting Dig Lookup Tool...")
                break
            if not self.is_valid_domain(domain):
                print("[!] Invalid domain. Please try again.")
                input("Press Enter to continue...")
                continue
            result = self.lookup(domain)
            print("\n" + result)
            choice = input("\nDo you want to perform another Dig lookup? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("[*] Exiting Dig Lookup Tool...")
                break

    def is_valid_domain(self, domain):
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9]'  
            r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)'  
            r'+[a-zA-Z]{2,6}$'
        )
        return domain_regex.match(domain)

    def lookup(self, domain):
        self.clear_screen()
        print(f"Performing DNS lookup for: {domain}\n")
        try:
            result = subprocess.run(["dig", domain], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"[!] Error performing DNS lookup: {e}")
            return f"Error: {e}"

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


class NmapTool:
    def __init__(self):
        self.nmapPrompt = "Enter IP/Domain for Nmap Scan (or type 'exit' to quit): "
        self.nmapLogo = """
        ====================================
        |            Nmap Tool             |
        ====================================
        """
        if not self.installed():
            print("[!] Nmap is not installed.")
            exit(1)
        self.run()

    def installed(self):
        return os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap")

    def run(self):
        while True:
            self.clear_screen()
            print(self.nmapLogo)
            target = input(self.nmapPrompt).strip()
            if target.lower() == 'exit':
                print("[*] Exiting Nmap Tool...")
                break
            if not self.is_valid_domain_or_ip(target):
                print("[!] Invalid IP or Domain. Please try again.")
                input("Press Enter to continue...")
                continue
            self.scan(target)
            choice = input("\nDo you want to perform another Nmap scan? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("[*] Exiting Nmap Tool...")
                break

    def is_valid_domain_or_ip(self, target):
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9]'  
            r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)'  
            r'+[a-zA-Z]{2,6}$'
        )
        ip_regex = re.compile(
            r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'  
        )
        return domain_regex.match(target) or ip_regex.match(target)

    def scan(self, target):
        self.clear_screen()
        print(f"Performing Nmap scan for: {target}\n")
        try:
            result = subprocess.run(["nmap", "-sV", target], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error performing Nmap scan: {e}")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


class TracerouteTool:
    def __init__(self):
        self.traceroutePrompt = "Enter IP/Domain for Traceroute (or type 'exit' to quit): "
        self.tracerouteLogo = """
        ====================================
        |         Traceroute Tool           |
        ====================================
        """
        if not self.installed():
            print("[!] Traceroute is not installed.")
            exit(1)
        self.run()

    def installed(self):
        return os.path.isfile("/usr/bin/traceroute") or os.path.isfile("/usr/local/bin/traceroute")

    def run(self):
        while True:
            self.clear_screen()
            print(self.tracerouteLogo)
            target = input(self.traceroutePrompt).strip()
            if target.lower() == 'exit':
                print("[*] Exiting Traceroute Tool...")
                break
            if not self.is_valid_domain_or_ip(target):
                print("[!] Invalid IP or Domain. Please try again.")
                input("Press Enter to continue...")
                continue
            self.perform_traceroute(target)
            choice = input("\nDo you want to perform another Traceroute? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("[*] Exiting Traceroute Tool...")
                break

    def is_valid_domain_or_ip(self, target):
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9]'  
            r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)'  
            r'+[a-zA-Z]{2,6}$'
        )
        ip_regex = re.compile(
            r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'  
        )
        return domain_regex.match(target) or ip_regex.match(target)

    def perform_traceroute(self, target):
        self.clear_screen()
        print(f"Performing Traceroute for: {target}\n")
        try:
            result = subprocess.run(["traceroute", target], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error performing Traceroute: {e}")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
        ====================================
        |        Information Gathering     |
        ====================================
        | 1 - Whois Lookup Tool            |
        | 2 - Dig Lookup Tool              |
        | 3 - Nmap Tool                    |
        | 4 - Traceroute Tool              |
        | 99 - Exit                        |
        ====================================
        """)
        choice = input("Choose a tool: ")
        if choice == "1":
            whois_tool = WhoisTool()
        elif choice == "2":
            dig_tool = DigTool()
        elif choice == "3":
            nmap_tool = NmapTool()
        elif choice == "4":
            traceroute_tool = TracerouteTool()
        elif choice == "99":
            print("[*] Exiting the tool...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
