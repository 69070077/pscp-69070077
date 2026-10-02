"""stock"""
def main():
    """stock"""
    num = int(input())
    even = 0
    odd = 0
    sums = 0
    for i in range(num):
        stock = int(input())
        sums += stock
        if not stock % 2:
            even += 1
        elif stock % 2:
            odd += 1
    i += 1
    print(f"SUM {sums}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")
main()
