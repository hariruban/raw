import whois
import argparse
import logging

# Configure logging
logging.basicConfig(filename='whois_tool.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        info = {
            "Domain": domain,
            "Registrar": w.registrar,
            "Creation Date": w.creation_date,
            "Expiration Date": w.expiration_date,
            "Updated Date": w.updated_date,
            "Name Servers": ', '.join(w.name_servers) if w.name_servers else 'N/A',
            "Status": ', '.join(w.status) if w.status else 'N/A',
            "Email": ', '.join(w.emails) if w.emails else 'N/A',
            "Address": w.address if w.address else 'N/A',
            "City": w.city if w.city else 'N/A',
            "State": w.state if w.state else 'N/A',
            "Country": w.country if w.country else 'N/A'
        }
        return info
    except Exception as e:
        logging.error(f"Error retrieving Whois information for {domain}: {e}")
        return None

def print_info(info):
    if info:
        print("\nWhois Information:")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("No information available.")

def main():
    parser = argparse.ArgumentParser(description="Advanced Whois Tool")
    parser.add_argument("domain", help="Domain name to query")
    args = parser.parse_args()

    domain = args.domain
    logging.info(f"Querying Whois information for {domain}")
    
    info = get_whois_info(domain)
    print_info(info)

if __name__ == "__main__":
    main()
