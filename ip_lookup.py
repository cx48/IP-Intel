import requests
from prettytable import PrettyTable
from collections import Counter
import os
import json
import random

# Optional API Token
IPINFO_TOKEN = None  # e.g., '56def'

headers = {
    "Authorization": f"Bearer {IPINFO_TOKEN}"
} if IPINFO_TOKEN else {}

def fetch_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            loc = data.get("loc", ",").split(",")
            return {
                "ip": data.get("ip", ip),
                "hostname": data.get("hostname", "N/A"),
                "country": data.get("country", "N/A"),
                "region": data.get("region", "N/A"),
                "city": data.get("city", "N/A"),
                "postal": data.get("postal", "N/A"),
                "latitude": loc[0] if len(loc) == 2 else "N/A",
                "longitude": loc[1] if len(loc) == 2 else "N/A",
                "asn": data.get("org", "N/A"),
            }
    except Exception:
        pass

    return {
        "ip": ip,
        "hostname": "N/A",
        "country": "N/A",
        "region": "N/A",
        "city": "N/A",
        "postal": "N/A",
        "latitude": "N/A",
        "longitude": "N/A",
        "asn": "N/A"
    }

def read_ips_from_file(file_path):
    if not os.path.isfile(file_path):
        print("❌ File not found.")
        return []
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_ip_input():
    print("📌 IP Lookup Tool")
    print("1. Enter IP(s) manually")
    print("2. Load IPs from file")
    choice = input("Select an option (1/2): ").strip()

    ip_list = []

    if choice == "1":
        ip_input = input("Enter IPs (comma-separated): ")
        ip_list = [ip.strip() for ip in ip_input.split(",") if ip.strip()]
    elif choice == "2":
        file_path = input("Enter file path: ").strip()
        ip_list = read_ips_from_file(file_path)
    else:
        print("Invalid option.")
    
    return ip_list

def save_json(data):
    os.makedirs("results", exist_ok=True)
    filename = f"report_{random.randint(1000, 9999)}.json"
    filepath = os.path.join("results", filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n💾 Saved JSON output to: {filepath}")

def main():
    ip_list = get_ip_input()
    if not ip_list:
        print("⚠️ No IPs provided.")
        return

    counter = Counter(ip_list)
    unique_ips = list(counter.keys())

    table = PrettyTable()
    table.field_names = [
        "IP Address", "Hostname", "Country", "Region", "City",
        "Postal Code", "Latitude", "Longitude", "ASN", "Count"
    ]

    result_data = []
    for ip in unique_ips:
        info = fetch_ip_info(ip)
        count = counter[ip]
        table.add_row([
            info["ip"], info["hostname"], info["country"],
            info["region"], info["city"], info["postal"],
            info["latitude"], info["longitude"], info["asn"],
            count
        ])
        info["count"] = count
        result_data.append(info)

    print("\n📊 IP Information:")
    print(table)

    save_json(result_data)

if __name__ == "__main__":
    main()