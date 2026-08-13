"""ink"""
import math
def main():
    """ink"""
    PI = 3.1416
    s, num = map(int, input().split())
    results = []
    for _ in range(num):
        x, y = map(int, input().split())
        time = (PI * (x**2 + y**2)) / s
        results.append(math.ceil(time))
    for res in results:
        print(res)
main()
