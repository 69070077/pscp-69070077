"""BirthDay"""
def main():
    """BirthDay"""
    year_1 = int(input())
    month_1 = int(input())
    day_1 = int(input())
    year_2 = int(input())
    month_2 = int(input())
    day_2 = int(input())

    if year_1 < year_2 and month_1 < month_2 and day_1 < day_2:
        print("1")
    elif year_2 < year_1 and month_2 < month_1 and day_2 < day_1:
        print("2")
    elif day_1 - day_2 <= 7 or day_2 - day_1 <= 7:
        print("0")
main()
