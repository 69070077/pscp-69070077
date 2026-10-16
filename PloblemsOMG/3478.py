"""Histogram"""
def main():
    """Histogram"""
    num = input()
    unit = []

    for i in range(26):
        unit.append(chr(97 + i))
        unit.append(chr(65 + i))

    for c in unit:
        num_count = num.count(c)
        if num_count > 0:
            print(f"{c} = {num_count}")
main()
