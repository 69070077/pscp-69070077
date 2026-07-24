"""Year"""
def main():
    """Year"""
    year = int(input())
    if not year % 100:
        if not year % 400:
            print("yes")
        else:
            print("no")
    elif not year % 4:
        print("yes")
    else:
        print("no")
main()
