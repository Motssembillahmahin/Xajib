import re


def find_pattern():
    text = input("Enter the text: ")

    pattern_to_find = input("Enter the pattern to find: ")

    matches = re.finditer(pattern_to_find, text)

    for match in matches:
        print(f"Pattern found at position {match.start()}-{match.end()}: {match.group()}")


find_pattern()