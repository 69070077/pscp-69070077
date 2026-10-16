"""MagicMaguc"""
def main():
    """Harry Potter"""
    num = int(input())

    total_fire = 0
    total_water = 0
    total_earth = 0

    for _ in range(num):
        x1, y1, z1, x2, y2, z2 = map(int, input().split())
        total_fire += max(x1, x2)
        total_water += max(y1, y2)
        total_earth += max(z1, z2)
    total_score = total_fire + total_water + total_earth
    BONUS = "YES" if total_fire > (total_water + total_earth) else "NO"

    print(f"Total: {total_score}")
    print(f"Fire: {total_fire}")
    print(f"Water: {total_water}")
    print(f"Earth: {total_earth}")
    print(f"Bonus: {BONUS}")
main()
