"""flashing"""
def main():
    """Flashing"""
    num = int(input())
    angle = [False] * 360

    for _ in range(num):
        a, b = map(int, input().split())
        if a < b:
            for k in range(a, b):
                angle[k] = True
        else:
            for k in range(a, 360):
                angle[k] = True
            for k in range(0, b):
                angle[k] = True
    if all(angle):
        print(360)
        return

    ans = 0
    run = 0
    for v in angle + angle:
        if v:
            run += 1
            ans = max(ans, run)
        else:
            run = 0
    print(ans)
main()
