"""Heron"""
import math
def main():
    """Heron"""
    a = float(input())
    b = float(input())
    c = float(input())
    if a >= 0:
        if b >= 0:
            if c >= 0:
                s = float((a + b + c) / 2)
                Area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
                print(f"{Area:.3f}")
    else:
        print("ERROR")
main()
