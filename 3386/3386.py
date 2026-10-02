"""Duplicate"""
def main():
    """Duplicate"""
    numA = int(input())
    numB = int(input())
    groupA = set()
    groupB = set()
    for _ in range(numA):
        groupA.add(int(input()))
    for _ in range(numB):
        groupB.add(int(input()))

    samenum = groupA & groupB
    if not samenum:
        print("Nope")
    else:
        for item in sorted(samenum, reverse=True):
            print(item)
main()
