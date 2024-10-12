import socket
import subprocess
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Clear the console screen (change 'clear' to 'cls' if on Windows)
subprocess.call('clear', shell=True)

# Get remote host input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print status
print("_" * 60)
print(f"Please wait, scanning remote host {remoteServerIP}")
print("_" * 60)

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Short timeout to speed up scanning
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                return port
    except:
        return None

# Start scanning
t1 = datetime.now()
open_ports = []

try:
    with ThreadPoolExecutor(max_workers=100) as executor:  # Adjust max_workers for concurrency
        futures = [executor.submit(scan_port, port) for port in range(1, 5000)]
        for future in as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# End scanning
t2 = datetime.now()
total = t2 - t1

# Print results
if open_ports:
    for port in open_ports:
        print(f"Port {port}: Open")
else:
    print("No open ports found.")

print(f"Scanning completed in: {total}")