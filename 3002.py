"""Password"""
def main():
    """Password"""
    name = input()
    ser = input()
    age = input()
    namel = len(name)
    serl = len(ser)
    if namel >= 5 and serl >= 5:
        print(name[0:2], ser[:-2:-1], age[:-2:-1], sep='')
    else:
        print(name[0:1], age, ser[:-2:-1], sep='')
main()
