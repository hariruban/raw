import os
import subprocess

class NmapTool:
    def __init__(self, toolDir):
        self.installDir = toolDir + "nmap"
        self.targetPrompt = "Enter Target IP/Subnet/Range/Host: "
        self.nmapLogo = """
        ====================================
        |           Nmap Scanner           |
        ====================================
        """
        if not self.installed():
            print("[!] Nmap is not installed.")
            exit(1)
        self.run()

    def installed(self):
        # Check if nmap is installed
        return os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap")

    def run(self):
        self.clear_screen()
        print(self.nmapLogo)
        target = input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        self.clear_screen()
        print(self.nmapLogo)
        print(f"   Nmap scan for: {target}\n")
        print("   {1}--Simple Scan [-sV]")
        print("   {2}--Firewall Scan [-Pn]")
        print("   {3}--Aggressive Scan [-A]\n")
        print("   {99}-Exit\n")
        response = input("nmap ~# ")
        self.clear_screen()
        
        try:
            if response == "1":
                subprocess.run(["nmap", "-sV", target])
                input("Press Enter to continue...")
            elif response == "2":
                subprocess.run(["nmap", "-Pn", target])
                input("Press Enter to continue...")
            elif response == "3":
                subprocess.run(["nmap", "-A", target])
                input("Press Enter to continue...")
            elif response == "99":
                return
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    toolDir = "/usr/local/src/"
    nmap_tool = NmapTool(toolDir)
