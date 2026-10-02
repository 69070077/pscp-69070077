"""Swapnum"""
def main():
    """Swapnum"""
    num = int(input())
    syb = input()
    numswap = int(str(num)[::-1])
    if syb == '+':
        total1 = num + numswap
        print(f"{num} + {numswap} = {total1}")
    elif syb == '*':
        total2 = num * numswap
        print(f"{num} * {numswap} = {total2}")
main()
