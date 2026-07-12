"""Password"""
def main():
    """Password"""
    name = input()
    ser = input()
    age = input()
    namel = len(name)
    if namel >= 5:
        print(name[0:2], ser[:-2:-1], age[1:2], sep='')
    else:
        print(name[0:1], age, ser[:-2:-1], sep='')
main()
