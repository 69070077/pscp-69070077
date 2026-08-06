"""BirthDay"""
from datetime import date
def main():
    """BirthDay"""
    year_1 = int(input())
    month_1 = int(input())
    day_1 = int(input())
    year_2 = int(input())
    month_2 = int(input())
    day_2 = int(input())

    who1 = date(year_1, month_1, day_1)
    who2 = date(year_2, month_2, day_2)
    whobirthbefore = abs((who1 - who2).days)

    if whobirthbefore <= 7:
        print("0")
    elif who1 < who2:
        print("1")
    elif who2 < who1:
        print("2")

main()
