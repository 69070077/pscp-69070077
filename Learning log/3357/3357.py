"""Giraffe"""
def main():
    """Giraffe"""
    num = int(input())
    height = []
    i = 0
    while i < num:
        height.append(int(input()))
        i += 1
    total = 0
    i = 0
    while i < num:
        if not i:
            if num == 1 or height[0] > height[1]:
                total += 1
        elif i == num - 1:
            if height[num - 1] > height[num - 2]:
                total += 1
        else:
            if height[i] > height[i - 1] and height[i] > height[i + 1]:
                total += 1
        i += 1
    print(total)
main()
