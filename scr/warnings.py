def count_warnings():
    warnings = []
    with open("sample.log", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "WARNING" in line:
                warnings.append(line)
    return warnings
