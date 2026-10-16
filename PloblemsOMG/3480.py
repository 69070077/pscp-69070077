"""NokNoy"""
def main():
    """NokNoy"""
    num = int(input())
    h = list(map(int, input().split()))
    ans = 0

    for i in range(num):
        left = (not i) or (h[i] > h[i - 1])
        right = (i == num - 1) or (h[i] > h[i + 1])
        if left and right:
            ans += 1
    print(ans)
main()
