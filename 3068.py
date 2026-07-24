"""Year"""
def main():
    """Year"""
    year = int(input())
    if not year % 400:
        print("yes")
    elif year <= 1582:
        print("yes")
    elif not year % 100:
        print("no")
    elif not year % 4:
        print("yes")
    else:
        print("no")
main()
