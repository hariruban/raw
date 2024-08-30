import os
import subprocess

class WhoisTool:
    def __init__(self):
        self.whoisPrompt = "Enter Domain or IP for Whois Lookup: "
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
        self.clear_screen()
        print(self.whoisLogo)
        target = input(self.whoisPrompt)
        self.lookup(target)

    def lookup(self, target):
        self.clear_screen()
        print(f"Performing Whois lookup for: {target}\n")
        try:
            subprocess.run(["whois", target])
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print("\n[!] Whois lookup interrupted by user.")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    whois_tool = WhoisTool()
