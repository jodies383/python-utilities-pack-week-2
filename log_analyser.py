import re

with open("system.log", "r") as file:
    log_data = file.read()

ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

ips = re.findall(ip_pattern, log_data)

for ip in ips:
    print(ip)
if "ERROR" in ip:
    print(ip)