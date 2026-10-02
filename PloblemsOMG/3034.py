"""Port"""
def main():
    """Port"""
    num, K = map(int, input().split())
    rows = [0] * (K + 1)
    ready_rows = 0
    for _ in range(num):
        q = int(input())
        if not rows[q]:
            ready_rows += 1
        rows[q] += 1
        if ready_rows == K:
            for i in range(1, K + 1):
                rows[i] -= 1
                if not rows[i]:
                    ready_rows -= 1
    print(sum(rows))
main()
