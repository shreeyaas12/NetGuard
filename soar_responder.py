import time
import re
import subprocess

LOG_FILE = "/var/log/suricata/fast.log"

def get_blocked_ips():
    result = subprocess.run(["sudo", "iptables", "-L", "INPUT", "-n"], capture_output=True, text=True)
    return set(re.findall(r'(\d+\.\d+\.\d+\.\d+)', result.stdout))

def block_ip(ip):
    blocked_ips = get_blocked_ips()
    if ip not in blocked_ips:
        print(f"[+] SOAR Action: Blocking Malicious IP -> {ip}")
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    else:
        print(f"[-] IP {ip} is already blocked.")

def monitor_logs():
    print("[*] SOAR Engine Started. Monitoring Suricata Logs...")
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue
            
            match = re.search(r'\{TCP\} (\d+\.\d+\.\d+\.\d+):\d+ ->', line)
            if match:
                src_ip = match.group(1)
                block_ip(src_ip)

if __name__ == "__main__":
    monitor_logs()
