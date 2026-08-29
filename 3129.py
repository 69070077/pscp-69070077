"""CoffeeShop"""
def main():
    """CoffeeShop"""
    num = int(input())
    firstday = int(input())
    max_income = firstday
    min_income = firstday
    total = firstday
    for _ in range(num-1):
        income = int(input())
        total += income
        if max_income < income:
            max_income = income
        if min_income > income:
            min_income = income
    print(total)
    print(max_income)
    print(min_income)
    print(round(total / num, 1))
main()
