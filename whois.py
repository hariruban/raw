import whois
import csv
import argparse
import logging
import os
import sys  # Import sys to handle sys.exit()

# Configure logging
logging.basicConfig(filename='whois_tool.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def query_whois(ip):
    """Query Whois information for a given IP address."""
    try:
        w = whois.whois(ip)
        return {
            "IP": ip,
            "Registrar": w.registrar if w.registrar else 'N/A',
            "Email": ', '.join(w.emails) if w.emails else 'N/A',
            "Name": w.name if w.name else 'N/A',
            "Country": w.country if w.country else 'N/A',
            "City": w.city if w.city else 'N/A'
        }
    except Exception as e:
        logging.error(f"Error retrieving Whois information for {ip}: {e}")
        return {
            "IP": ip,
            "Registrar": 'Error',
            "Email": 'Error',
            "Name": 'Error',
            "Country": 'Error',
            "City": 'Error'
        }

def process_single_ip(ip, outfile):
    """Process a single IP address and write the result to a CSV file."""
    info = query_whois(ip)
    outfile.writerow(info.values())
    print(f"Processed IP: {ip}")

def process_ip_list(file_path, outfile):
    """Process a list of IP addresses from a file and write results to a CSV file."""
    if not os.path.isfile(file_path):
        logging.error(f"File {file_path} does not exist.")
        print(f"Error: File {file_path} does not exist.")
        return

    with open(file_path, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip:
                info = query_whois(ip)
                outfile.writerow(info.values())
                print(f"Processed IP: {ip}")

def main():
    parser = argparse.ArgumentParser(description="Advanced Whois Tool")
    parser.add_argument('-i', '--ip', help="Single IP address to query", type=str)
    parser.add_argument('-l', '--list', help="File path to a list of IP addresses", type=str)
    args = parser.parse_args()

    if not args.ip and not args.list:
        print("Error: You must provide either a single IP address or a file path to a list of IP addresses.")
        parser.print_help()
        sys.exit(1)  # Exit if neither argument is provided

    with open("output.csv", "w", newline='') as csvfile:
        outfile = csv.writer(csvfile)
        outfile.writerow(['IP', 'Registrar', 'Email', 'Name', 'Country', 'City'])

        if args.ip:
            process_single_ip(args.ip, outfile)
        elif args.list:
            process_ip_list(args.list, outfile)

    print('Done')

if __name__ == "__main__":
    main()
