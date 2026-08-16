"""inflation"""
def main():
    """inflation"""
    money = int(input())
    year = int(input())
    inf = 0.0381
    for _ in range(year):
        money = int(money * (1 + inf)*100) / 100
    print(f"{money:.2f}")
main()
