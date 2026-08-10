"""Tax Car"""
def main():
    """Tax Car"""
    year = int(input())
    engine = int(input())

    if 0 < year <= 1990:
        if engine <= 1500:
            print("1250")
        elif 1500 < engine <= 2000:
            print("1400")
        elif engine > 2000:
            print("2000")
    elif 1991 <= year <= 1999:
        if engine <= 1500:
            print("1100")
        elif 1500 < engine <= 2000:
            print("1300")
        elif engine > 2000:
            print("1700")
    elif year >= 2000:
        if engine <= 1500:
            print("1000")
        elif 1500 < engine <= 2000:
            print("1200")
        elif engine > 2000:
            print("1500")
main()
