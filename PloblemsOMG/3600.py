"""CalCal"""
def main():
    """CalCal"""
    cal = {
        1:100,
        2:120,
        3:200,
        4:60
    }
    total_cal = 0
    while True:
        num = int(input())
        if num == 5:
            break
        total_cal += cal.get(num, 0)

    print("Bye Bye")
    print(f"Total Calories: {total_cal}")
main()
