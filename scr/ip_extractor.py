import re

def find_ips():
    ips = set()
    with open("sample.log", "r") as file:
        lines = file.readlines()
        for line in lines:
            found_ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            for ip in found_ips:
                ips.add(ip)

    with open("reports/ips.txt", "w") as f:
        for ip in ips:
            f.write(ip + "\n")

    return ips