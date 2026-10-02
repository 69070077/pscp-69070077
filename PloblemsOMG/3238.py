"""Elon"""
def main():
    """Elon"""
    word = input().strip()

    if " " in word:
        part = word.split()
        x = int(part[0])
        k = part[1]
    else:
        x = int(word[:-1])
        k = word[-1]

    middle = x // 2
    for i in range(x):
        row = ["-"] * x
        if k == "#":
            char = "#"
        else:
            dist = abs(i - middle)
            char = chr(ord(k) + dist)
        row[i] = char
        row[x - 1 - i] = char
        print("".join(row))
main()
