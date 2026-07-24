"""DivideTen"""
def main():
    """DivideTen"""
    num = int(input())
    while num > 0:
        if not num % 10:
            print(num, end=" ")
        num -= 1
    print("0")
main()
