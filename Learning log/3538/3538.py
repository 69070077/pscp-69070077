"""B-Fully"""
def main():
    """B-Fully"""
    pair = input()
    nopair = ""
    text_check = []
    for char in pair:
        if char not in text_check:
            text_check.append(char)
            count = pair.count(char)
            if count % 2:
                nopair += char

    if not nopair:
        print("fully paired")
    else:
        print(nopair)
main()
