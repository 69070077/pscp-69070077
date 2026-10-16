"""TumBonBullet"""
def main():
    """TumBonBullet"""
    num = int(input())
    shot = []

    for _ in range(num):
        x, y, d = map(int, input().split())
        shot.append((x, y, d))

    for tx in range(1001):
        for ty in range(1001):
            ok = True
            for x, y, d in shot:
                if (x - tx) ** 2 + (y - ty) ** 2 != d * d:
                    ok = False
                    break
            if ok:
                print(f"{tx} {ty}")
                return
main()
