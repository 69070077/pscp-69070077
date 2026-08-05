"""Promotion"""
def main():
    """Promotion"""
    item = input()
    items = item.split()
    pencil = int(items[0])
    book = int(items[1])
    color = int(items[2])
    itemtotal = pencil + book + color
    if itemtotal >= 3:
        totalprice = (pencil * 25) + (book * 40) + (color * 55)
        discount = totalprice * 0.1
        totalprice = totalprice - discount
        print(int(totalprice))
    elif itemtotal < 3:
        totalprice = (pencil * 25) + (book * 40) + (color * 55)
        print(int(totalprice))
main()
