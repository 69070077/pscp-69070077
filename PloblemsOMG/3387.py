"""TupleSad"""
def main():
    """TupleSad"""
    numbers = tuple(input().split())
    num = input()

    position = str(numbers.index(num))
    size = numbers.count(num)

    for _ in range(size):
        row = " ".join([position] * size)
        print(row)
main()
