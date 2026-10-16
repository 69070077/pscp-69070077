"""kairod"""
def main():
    """kairod"""
    num = int(input())
    x = []
    i = 0

    while i < num:
        spec = input().split()[1]
        x.append(int(spec))
        i += 1
    ans = 0
    mx = -1
    i = num - 1
    while i >= 0:
        if x[i] < mx:
            ans += 1
        else:
            mx = x[i]
        i -= 1
    print(ans)
main()
