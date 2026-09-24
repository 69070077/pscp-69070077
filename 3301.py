"""PutintheBox"""
def main():
    """PutintheBox"""
    w, l, r, a = map(int, input().split())
    box = []

    for i in range(r, a + 1):
        f = w % i
        s = l % i
        box.append(f * s)

    print(min(box))

main()
