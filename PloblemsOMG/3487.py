"""ChangFai"""
def main():
    """ChangFai"""
    num = int(input())
    height = [int(input()) for _ in range(num)]
    height.sort()
    total = 0
    prefix = 0

    for i in height:
        prefix += i
        total += prefix
    print(total * 2)
main()
