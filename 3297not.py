"""TicTicket"""
def main():
    """TicTicket"""
    seats = int(input())
    i = 0
    while i < seats:
        age, num = input().split()
        age = int(age)
        num = int(num)
        if age > 15:
            if 15 <= age <= 22:
                price = 150 - (150*0.2)
                total = price * num
                print(f"{total} {num}")
            elif age > 60:
                price = 150 - (150*0.5)
                total = price * num
                print(f"{total} {num}")
        i += num
main()
