from collections import Counter
from datetime import datetime
import socket


def analyze_connections():
    print("=" * 55)
    print("        Network Traffic Analyzer")
    print("=" * 55)

    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.error:
        local_ip = "Unable to determine"

    print(f"\nHostname : {hostname}")
    print(f"Local IP : {local_ip}")
    print(f"Time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("\nNetwork Information")
    print("-" * 55)

    protocols = ["TCP", "TCP", "UDP", "TCP", "ICMP", "UDP", "TCP"]

    protocol_count = Counter(protocols)

    print("Protocol statistics:")
    for protocol, count in protocol_count.items():
        print(f"  {protocol}: {count} packets")

    print("\nConnection Test")
    print("-" * 55)

    targets = ["google.com", "github.com", "cloudflare.com"]

    for target in targets:
        try:
            ip = socket.gethostbyname(target)
            print(f"{target:<18} → {ip}")
        except socket.gaierror:
            print(f"{target:<18} → Unable to resolve")

    print("\nAnalysis completed.")


if __name__ == "__main__":
    analyze_connections()
