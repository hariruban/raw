import os
import subprocess

class NmapTool:
    def __init__(self, toolDir):
        self.installDir = os.path.join(toolDir, "nmap")
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
        if target:
            self.menu(target)
        else:
            print("[!] No target specified. Exiting.")
            exit(1)

    def menu(self, target):
        while True:
            self.clear_screen()
            print(self.nmapLogo)
            print(f"   Nmap scan for: {target}\n")
            print("   {1}--Simple Scan [-sV]")
            print("   {2}--Firewall Scan [-Pn]")
            print("   {3}--Aggressive Scan [-A]")
            print("   {4}--Port Scan [-p PORTS]")
            print("   {5}--OS Detection [-O]")
            print("   {6}--Custom Scan")
            print("   {99}-Exit\n")
            response = input("nmap ~# ")
            self.clear_screen()
            
            try:
                if response == "1":
                    self.run_scan(target, ["-sV"])
                elif response == "2":
                    self.run_scan(target, ["-Pn"])
                elif response == "3":
                    self.run_scan(target, ["-A"])
                elif response == "4":
                    ports = input("Enter ports (e.g., 80,443): ")
                    self.run_scan(target, ["-p", ports])
                elif response == "5":
                    self.run_scan(target, ["-O"])
                elif response == "6":
                    custom_options = input("Enter custom Nmap options: ")
                    self.run_scan(target, custom_options.split())
                elif response == "99":
                    exit(0)
                else:
                    print("[!] Invalid option. Please try again.")
                
                # Ask if the user wants to perform another scan
                self.restart_prompt()
                
            except KeyboardInterrupt:
                print("\nInterrupted. Returning to menu...")
            except Exception as e:
                print(f"An error occurred: {e}")
                self.restart_prompt()

    def run_scan(self, target, options):
        command = ["nmap"] + options + [target]
        subprocess.run(command)
        input("Press Enter to return to the menu...")

    def restart_prompt(self):
        response = input("\nDo you want to perform another scan? (yes/no): ").strip().lower()
        if response == "yes":
            self.run()
        elif response == "no":
            exit(0)
        else:
            print("[!] Invalid response. Exiting.")
            exit(1)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    toolDir = "/usr/local/src/"
    nmap_tool = NmapTool(toolDir)
