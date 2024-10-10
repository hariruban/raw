import subprocess

def run_nikto(target):
    try:
        print(f"Starting Nikto scan for {target}...\n")
        # Run Nikto as a subprocess
        result = subprocess.run(['nikto', '-h', target], capture_output=True, text=True)
        
        # Print the output of Nikto scan
        if result.returncode == 0:
            print("Nikto Scan Results:\n")
            print(result.stdout)
        else:
            print("Nikto scan failed with the following error:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = input("Enter target URL for Nikto scan (e.g., http://example.com): ")
    run_nikto(target)
