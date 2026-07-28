"""Lowest 4"""
def main():
    """Lowest 4"""
    i = 0
    num = []
    while i < 4:
        num.append(int(input()))
        i += 1
    num.sort()
    print(num[0])
main()
