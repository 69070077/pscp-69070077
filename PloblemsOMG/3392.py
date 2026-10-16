"""Funnyarray"""
def main():
    """yarraynnuf"""
    num = []

    for i in range(1, 4):
        value = int(input())
        num.append(value)
        print(f"Input number {i} stored.")

    while True:
        menu = int(input())
        if not menu:
            break
        if menu == 1:
            RES = " ".join(map(str, num))
            print(f"Original order: {RES}")
        elif menu == 2:
            desc = sorted(num, reverse=True)
            RES = " ".join(map(str, desc))
            print(f"Descending order: {RES}")
        elif menu == 3:
            asc = sorted(num)
            RES = " ".join(map(str, asc))
            print(f"Ascending order: {RES}")
main()
