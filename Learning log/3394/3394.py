"""PassTor"""
def main():
    """PassTor"""
    n, s = map(int, input().split())
    next_man = [0] * (n + 1)

    for i in range(1, n + 1):
        next_man[i] = int(input())
    seen = set()
    current = s

    while current and current not in seen:
        seen.add(current)
        current = next_man[current]
    print(len(seen))
main()
