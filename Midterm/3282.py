"""Stats"""
def main():
    """Stats"""
    num = int(input())
    firstnum = int(input())
    maxnum = firstnum
    minnum = firstnum
    total = firstnum
    for _ in  range(num-1):
        xnum = int(input())
        if maxnum < xnum:
            maxnum = xnum
        if minnum > xnum:
            minnum = xnum
        total += xnum
    print(f"MIN: {minnum:.3f}")
    print(f"MAX: {maxnum:.3f}")
    print(f"AVG: {total/num:.3f}")
main()
