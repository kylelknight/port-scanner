import socket
from datetime import datetime

def port_scanner(target_ip, start_port, end_port):
    print(f"Starting scan on host: {target_ip}")
    start_time = datetime.now()
    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port}: Open")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except socket.gaierror:
        print("\nHostname could not be resolved.")
    except socket.error:
        print("\nCouldn't connect to server.")
    finally:
        end_time = datetime.now()
        total_time = end_time - start_time
        print(f"\nScanning completed in: {total_time}")

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    start_port = 1
    end_port = 1024
    port_scanner(target, start_port, end_port)
