"""AVGscore"""
def main():
    """AVGscore"""
    num = int(input())
    total = 0
    ispass = True
    for _ in range(num):
        score = int(input())
        total += score
        if score < 50:
            ispass = False
    avgscore = total / num
    print(f"{avgscore:.1f}")
    if ispass is False:
        print("FAIL")
    elif ispass is True:
        if avgscore >= 60.0:
            print("PASS")
        else:
            print("FAIL")
main()
