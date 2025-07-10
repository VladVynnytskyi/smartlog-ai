errors = []
warn = []

def readlog():
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

if __name__ == "__main__":
    ask = int(input("Choose options, print 1 or 2 or 3\n"
                    "1) Errors\n"
                    "2) Warnings\n"
                    "3) ...\n"))

    if ask == 1:
        readlog()
        print(errors)
    elif ask == 2:
        count_warnings()
        print(warn)
    elif ask == 3:
        print()
    else:
        print("Choose correct option")
