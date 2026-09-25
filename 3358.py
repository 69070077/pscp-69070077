"""Pig"""
def main():
    """Pig"""
    num = int(input())
    piggy_all = input().split()
    maxpig = []
    total = 0
    for _ in range(num):
        pig1 = int(piggy_all[0])
        pig2 = int(piggy_all[1])
        if pig1 >= pig2:
            maxpig.append(pig1)
            total += pig1
        else:
            maxpig.append(pig2)
            total += pig2
        piggy_all.pop(0)
        piggy_all.pop(0)
    if num == 1:
        print(total)
    else:
        print(f"{" + ".join(map(str , maxpig))} = {total}")
main()
