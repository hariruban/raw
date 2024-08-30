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
        # Check if whois is installed
        return os.path.isfile("/usr/bin/whois") or os.path.isfile("/usr/local/bin/whois")

    def run(self):
        while True:
            self.clear_screen()
            print(self.whoisLogo)
            target = input(self.whoisPrompt).strip()

            # Check if the user wants to exit
            if target.lower() == 'exit':
                print("[*] Exiting Whois Lookup Tool...")
                break

            # Validate the input
            if not self.is_valid_domain_or_ip(target):
                print("[!] Invalid domain or IP address. Please try again.")
                input("Press Enter to continue...")
                continue

            # Perform the whois lookup and display the result
            result = self.lookup(target)
            print("\n" + result)

            # Ask the user whether to perform another scan or exit
            choice = input("\nDo you want to perform another Whois lookup? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("[*] Exiting Whois Lookup Tool...")
                break

    def is_valid_domain_or_ip(self, target):
        # Validate if the target is a valid domain or IP address
        domain_regex = re.compile(
            r'^(?:[a-zA-Z0-9]'  # First character of the domain
            r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)'  # Sub domain + hostname
            r'+[a-zA-Z]{2,6}$'  # First level TLD
        )
        ip_regex = re.compile(
            r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'  # IPv4
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

if __name__ == "__main__":
    whois_tool = WhoisTool()
