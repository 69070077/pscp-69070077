"""Christmas"""
def main():
    """Christmas"""
    start_color, count = input().split()
    count_int = int(count)
    allcolor = ["Red", "Green", "Blue"]

    if start_color == "R":
        start = 0
    elif start_color == "G":
        start = 1
    else:
        start = 2

    total_color = []
    for i in range(count_int):
        colors = allcolor[(start + i) % 3]
        total_color.append(colors)
    print(*total_color)
main()
