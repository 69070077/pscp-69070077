"""PointSort"""
def main():
    """PointSort"""
t = int(input())

for _ in range(t):
    num = int(input())
    point = []
    for _ in range(num):
        x, y = map(int, input().split())
        point.append((x, y))
    point.sort(key=lambda p: (p[0] + p[1], -p[1]))
    for x, y in point:
        print(x, y)
main()
