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

class NiktoTool:
    def __init__(self):
        self.niktoPrompt = "Enter target URL for Nikto scan (e.g., http://example.com, or type 'exit' to quit): "
        self.niktoLogo = """
        ====================================
        |          Nikto Tool              |
        ====================================
        """
        if not self.installed():
            print("[!] Nikto is not installed.")
            exit(1)
        self.run()

    def installed(self):
        return os.path.isfile("/usr/bin/nikto.pl") or os.path.isfile("/usr/local/bin/nikto.pl")

    def run(self):
        while True:
            self.clear_screen()
            print(self.niktoLogo)
            target = input(self.niktoPrompt).strip()
            if target.lower() == 'exit':
                print("[*] Exiting Nikto Tool...")
                break
            if not self.is_valid_url(target):
                print("[!] Invalid URL. Please try again.")
                input("Press Enter to continue...")
                continue
            self.scan(target)
            choice = input("\nDo you want to perform another Nikto scan? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("[*] Exiting Nikto Tool...")
                break

    def is_valid_url(self, url):
        url_regex = re.compile(
            r'^(http://|https://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(/[a-zA-Z0-9-./?%&=]*)?$'
        )
        return url_regex.match(url)

    def scan(self, target):
        self.clear_screen()
        print(f"Performing Nikto scan for: {target}\n")
        try:
            result = subprocess.run(["perl", "/usr/bin/nikto.pl", "-h", target], capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error performing Nikto scan: {e}")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


class InfoGatheringTool:
    def __init__(self):
        self.logo = """
        ====================================
        |      Information Gathering Tool   |
        ====================================
        """
        self.run()

    def run(self):
        while True:
            self.clear_screen()
            print(self.logo)
            print("Select an option:")
            print("1. Whois Lookup")
            print("2. DNS Lookup (Dig)")
            print("3. Nmap Scan")
            print("4. Traceroute")
            print("5. Nikto Scan")
            print("6. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                WhoisTool()
            elif choice == '2':
                DigTool()
            elif choice == '3':
                NmapTool()
            elif choice == '4':
                TracerouteTool()
            elif choice == '5':
                NiktoTool()
            elif choice == '6':
                print("[*] Exiting Information Gathering Tool...")
                break
            else:
                print("[!] Invalid choice. Please try again.")
                input("Press Enter to continue...")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    InfoGatheringTool()
