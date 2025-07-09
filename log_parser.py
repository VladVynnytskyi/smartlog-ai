errors = []

# ask = int(input("Choose options, print 1 or 2 or 3 1)errors/2).../3).../ "))

def readlog():
    with open("sample.log", "r") as file:
        lines = file.readlines()
        for line in lines: #!!!!
            if "ERROR" in line:
                errors.append(line)

if __name__=="__main__": #Якщо ти запустиш log_parser.py напряму — код у if __name__ == "__main__" виконається, Якщо ж ти імпортуєш його через import log_parser у main.py — код НЕ виконається.
    readlog()
    print(errors)
