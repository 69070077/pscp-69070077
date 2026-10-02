"""Set"""
def main():
    """Difference"""
    numA = int(input())
    numB = int(input())
    setA = set()
    setB = set()

    for _ in range(numA):
        setA.add(int(input()))
    for _ in range(numB):
        setB.add(int(input()))

    ans = sorted(setA - setB)
    print(*(ans))
main()
