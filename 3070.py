"""EvenOdd"""
def main():
    """EvenOdd"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    evennum = 0
    oddnum = 0
    if not num1 % 2:
        evennum += 1
    elif num1 % 2:
        oddnum += 1
    if not num2 % 2:
        evennum += 1
    elif num2 % 2:
        oddnum += 1
    if not num3 % 2:
        evennum += 1
    elif num3 % 2:
        oddnum += 1
    print(evennum, oddnum, sep="\n")
main()
