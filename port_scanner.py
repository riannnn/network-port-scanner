import socket
import sys

def scan(target, ports):
    print(f"\nScanning target: {target}\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()

        except KeyboardInterrupt:
            print("\nScan stopped.")
            sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <target>")
    else:
        target_host = sys.argv[1]
        common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306]
        scan(target_host, common_ports)
