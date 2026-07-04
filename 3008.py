"""Heron"""
def main():
    """Heron"""
    a = int(input())
    b = int(input())
    c = int(input())
    if a >= 0:
        if b >= 0:
            if c >= 0:
                s = (a + b + c) / 2
                Area = (s*((s-a)*(s-b)*(s-c)))**0.5
                print(f"{Area:.3f}")
    else:
        print("ERROR")
main()
