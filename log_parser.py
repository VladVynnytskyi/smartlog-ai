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


if __name__ == "__main__":
    ask = int(input("Choose options, print 1 or 2 or 3\n"
                    "1) Errors\n"
                    "2) Warnings\n"
                    "3) Ips \n"))

    if ask == 1:
        read_log()
        print(errors)
    elif ask == 2:
        count_warnings()
        print(warn)
    elif ask == 3:
        find_ips()
    else:
        print("Choose correct option")
