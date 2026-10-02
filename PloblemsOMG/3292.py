"""Arrow"""
def main():
    """Arrow"""
    direct = input()
    scale = int(input())
    total = 2*scale - 1
    mid = total // 2
    for char in direct:
        if char == "R":
            for i in range(total):
                space = 2 * (mid - abs(i - mid))
                print(" " * space + "*" * (1 + abs(i - mid)))
        elif char == "L":
            for i in range(total):
                space = 1 * abs(i - mid)
                print(" " * space + "*" * (1 + abs(i - mid)))
        print("")
main()
