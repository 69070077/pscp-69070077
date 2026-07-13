"""season"""
def main():
    """season"""
    month = int(input())
    day = int(input())
    if 1 <= month <= 3:
        print("winter")
        if month == 3 and day >= 21:
            print("spring")
    if 3 < month <= 6:
        print("spring")
        if month == 6 and day >= 21:
            print("summer")
    if 6 < month <= 9:
        print("summer")
        if month == 9 and day >= 21:
            print("fall")
    if 9 < month <= 12:
        print("fall")
        if month == 12 and day >= 21:
            print("winter")
main()
