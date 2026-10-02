"""GCD_N"""
import math
def main():
    """GCD_N"""
    num = int(input())
    numbers = []
    for _ in range(num):
        numbers.append(int(input()))

    current_num = numbers[0]

    for i in range(1, num):
        current_num = math.gcd(current_num, numbers[i])

    print(current_num)
main()
