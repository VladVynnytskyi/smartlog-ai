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