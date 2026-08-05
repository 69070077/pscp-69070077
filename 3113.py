"""Ramen"""
def main():
    """Ramen"""
    size_type = input()
    size_type.split()
    size_ramen = size_type[0]
    type_ramen = size_type[1]

    topping = input()
    toppings = topping.split(" ")
    topping_s = str(toppings[0])
    piece = int(toppings[1])

    price = 0
    mhu = 15
    egg = 10

    if size_ramen == "S":
        if type_ramen == "R":
            price = 60
            if topping_s == "P":
                price + (mhu * piece)
                print(price)
            elif topping_s == "E":
                price + (egg * piece)
                print(price)
            elif topping_s == "N":
                print(price)
        elif type_ramen == "T":
            price = 80
            if topping_s == "P":
                price + (mhu * piece)
                print(price)
            elif topping_s == "E":
                price + (egg * piece)
                print(price)
            elif topping_s == "N":
                print(price)
    elif size_ramen == "M":
        if type_ramen == "R":
            price = 80
            if topping_s == "P":
                price + (mhu * piece)
                print(price)
            elif topping_s == "E":
                price + (egg * piece)
                print(price)
            elif topping_s == "N":
                print(price)
        elif type_ramen == "T":
            price = 100
            if topping_s == "P":
                price + (mhu * piece)
                print(price)
            elif topping_s == "E":
                price + (egg * piece)
                print(price)
            elif topping_s == "N":
                print(price)
    elif size_ramen == "L":
        if type_ramen == "R":
            price = 100
            if topping_s == "P":
                price + (mhu * piece)
                print(price)
            elif topping_s == "E":
                price + (egg * piece)
                print(price)
            elif topping_s == "N":
                print(price)
        elif type_ramen == "T":
            price = 120
            if topping_s == "P":
                price + (mhu * piece)
                print(price)
            elif topping_s == "E":
                price + (egg * piece)
                print(price)
            elif topping_s == "N":
                print(price)
main()
