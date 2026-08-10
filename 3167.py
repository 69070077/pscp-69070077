"""FizzBuzz"""
def main():
    """FizzBuzz"""
    n = int(input())
    num = 1
    for _ in range(n):
        if not num % 3 and not num % 5:
            print("FizzBuzz")
        elif not num % 5:
            print("Buzz")
        elif not num % 3:
            print("Fizz")
        else:
            print(num)
        num += 1
main()
