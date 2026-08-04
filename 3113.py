"""Ramen"""
def main():
    """Ramen"""
    size_type = input()
    size_type.split()
    size_ramen = size_type[0]
    type_ramen = size_type[1]

    topping = input()
    topping.split()
    topping_s = topping[0]
    piece = int(topping[1])

    price = 0
    mhu = 15
    egg = 10

    if size_ramen == "S":
        if type_ramen == "R":
            price = 60
        elif type_ramen == "T":
            price = 80
            if topping_s == "P":
                total = price + (mhu * piece)
            elif topping_s == "E":
                total = price + (egg * piece)
            elif topping_s == "N":
                total = price
            
main()



