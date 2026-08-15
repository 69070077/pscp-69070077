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
    if ispass is False:
        print(avgscore)
        print("FAIL")
    elif ispass is True:
        if avgscore > 50.0:
            print(avgscore)
            print("PASS")
        else:
            print(avgscore)
            print("FAIL")
main()
