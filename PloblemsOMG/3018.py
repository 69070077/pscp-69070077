"""Rectangle"""
def main():
    """Rectangle"""
    ax, ay, aw, ah = list(map(int, input().split()))
    bx, by, bw, bh = list(map(int, input().split()))

    width = max(0, min(ax + aw, bx + bw) - max(ax, bx))
    height = max(0, min(ay + ah, by + bh) - max(ay, by))
    area = width * height

    if area > 0:
        print(area)
    else:
        print("no overlapping")
main()
