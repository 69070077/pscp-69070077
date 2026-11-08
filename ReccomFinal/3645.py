"""Korjailagturbo"""
def main():
    """Korjailagturbo"""
    number = input()
    typenum = input()
    if typenum == "International":
        number = number.replace("0", "+66", 1)
    last = number[-4:]
    mid = number[-8:-4]
    front = number[:-8]
    print(front, mid, last)
main()
