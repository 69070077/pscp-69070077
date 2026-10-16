"""TankAKAH"""
def main():
    """TankKAYAH"""
    num = int(input())

    for _ in range(num):
        p = input().split()
        w1, w2, w3 = float(p[0]), float(p[1]), float(p[2])
        total = w1 + w2 + w3
        res = f"{total:.1f}"

        kayah = []
        if total > 50.0:
            kayah.append("Overloaded")

        if w1 > 20.0:
            kayah.append("Check Type Plastic")
        if w2 > 20.0:
            kayah.append("Check Type Can")
        if w3 > 20.0:
            kayah.append("Check Type Glass")
        if kayah:
            res += ", " + ", ".join(kayah)
        print(res)
main()
