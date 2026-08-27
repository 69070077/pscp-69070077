"""Ramen"""
def main():
    """Ramen"""
    size_ramen, type_ramen = input().split()
    topping = input().split()
    topping_type = topping[0]
    price = 0
    piece = 0
    if len(topping) > 1:
        piece = int(topping[1])
    if size_ramen == "S":
        if type_ramen == "R":
            price = 60
        elif type_ramen == "T":
            price = 80
    if size_ramen == "M":
        if type_ramen == "R":
            price = 80
        elif type_ramen == "T":
            price = 100
    if size_ramen == "L":
        if type_ramen == "R":
            price = 100
        elif type_ramen == "T":
            price = 120

    if topping_type == "P":
        price += 15 * piece
    elif topping_type == "E":
        price += 10 * piece
    print(price)
main()
