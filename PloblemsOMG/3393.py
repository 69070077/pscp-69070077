"""CaveMan"""
def main():
    """CaveMan"""
    num = int(input())
    cave = list(map(int, input().split()))
    cmd = input().strip()

    position = -1
    chest = -1
    for i in range(num):
        if cave[i] == 1:
            position = i
        if cave[i] == 2:
            chest = i

    cave[position] = 0
    found_chest = False
    for c in cmd:
        if not found_chest:
            if c == 'L' and position > 0:
                position = position - 1
            elif c == 'R' and position < num - 1:
                position = position + 1

            if position == chest:
                found_chest = True

    cave[position] = 1
    for i in range(num):
        if i == num - 1:
            print(cave[i])
        else:
            print(cave[i], end=" ")
main()
