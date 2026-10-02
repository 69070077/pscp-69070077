"""Exchange"""
def main():
    """Exchange"""
    money = int(input())
    sibbaht = money // 10
    moneyleft = money % 10

    fivebaht = moneyleft // 5
    moneyleft2 = moneyleft % 5

    twobaht = moneyleft2 // 2
    moneyleft3 = moneyleft2 % 2

    onebaht = moneyleft3 // 1

    print(f"10 = {sibbaht}")
    print(f"5 = {fivebaht}")
    print(f"2 = {twobaht}")
    print(f"1 = {onebaht}")
main()
