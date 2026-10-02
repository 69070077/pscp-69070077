"""Total of mostest value"""
def main():
    """Total of mostest value"""
    num = int(input())
    total = 0
    maxnum = []
    for _ in range(num):
        x = int(input())
        y = int(input())
        if x > y:
            total += x
            maxnum.append(str(x))
        else:
            total += y
            maxnum.append(str(y))
    if num == 1:
        if x > y:
            print(x)
        else:
            print(y)
    else:
        text = " + ".join(maxnum)
        print(f"{text} = {total}")
main()
