"""texi"""
def main():
    """Texi"""
    distance = int(input())
    if 0 < distance <= 1:
        print("35")
    elif not distance :
        print("0")
    i = 0
    price = 35
    total = 0
    if 1 < distance <= 10:
        while i < distance:
            total = (price + (distance * 5))-5
            i += 1
        print(total)
    if distance > 10:
        while i < distance:
            total2 = total + (distance * 8)
            i += 1
        print(total2)
main()