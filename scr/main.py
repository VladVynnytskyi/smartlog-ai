from scr.reader import read_log
from scr.warnings import count_warnings
from scr.ip_extractor import find_ips
from scr.search import search_keyword

def main():
    ask = int(input("Choose options, print 1 or 2 or 3 or 4\n"
                    "1) Errors\n"
                    "2) Warnings\n"
                    "3) IPs\n"
                    "4) Search keyword\n"))

    if ask == 1:
        errors = read_log()
        print(errors)
    elif ask == 2:
        warnings = count_warnings()
        print(warnings)
    elif ask == 3:
        ips = find_ips()
        print(ips)
    elif ask == 4:
        keyword = input("Enter keyword to search:")
        search_keyword(keyword)
    else:
        print("Choose correct option")

if __name__ == "__main__":
    main()
