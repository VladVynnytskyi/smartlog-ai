import re

def read_log():
    errors = []
    with open("sample.log", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "ERROR" in line:
                errors.append(line)
    return errors