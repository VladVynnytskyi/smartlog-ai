import re

errors = []
warn = []

def read_log():
    with open("sample.log", "r") as file:
        lines = file.readlines()
    for line in lines:
        if "ERROR" in line:
            errors.append(line)

def count_warnings():
    with open("sample.log", "r") as file:
        lines = file.readlines()
    for line in lines:
        if "WARNING" in line:
            warn.append(line)

def find_ips():
    with open("sample.log", "r") as file:
        lines = file.readlines()
    ips = set()
    for line in lines:
        found_ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
        for ip in found_ips:
            ips.add(ip)

    print(ips)

    with open("ips.txt", "w") as f:
        for ip in ips:
            f.write(ip + "\n")

    return ips


def search_keyword(keyword):
    with open("sample.log", "r") as file:
        lines = file.readlines()

    found = []
    for line in lines:
        if keyword.lower() in line.lower():  
            found.append(line.strip())

    if found:
        print(f"\nFound {len(found)} lines containing '{keyword}':\n")
        for line in found:
            print(line)
    else:
        print(f"\nNo matches found for '{keyword}'.")


if __name__ == "__main__":
    ask = int(input("Choose options, print 1 or 2 or 3\n"
                    "1) Errors\n"
                    "2) Warnings\n"
                    "3) IPs\n"
                    "4) Search keyword\n"))

    if ask == 1:
        read_log()
        print(errors)
    elif ask == 2:
        count_warnings()
        print(warn)
    elif ask == 3:
        ips = find_ips()
    elif ask == 4:
        keyword = input("Enter keyword to search:")
        search_keyword(keyword)
    else:
        print("Choose correct option")

    print(f"Errors: {len(errors)}, Warnings: {len(warn)}, IPs: {len(ips) if 'ips' in locals() else 0}")
