"""Rabbit"""
def main():
    """Rabbit"""
    veg = input()
    vegs = veg.split(" ")
    carrot = int(vegs[0])
    cab = int(vegs[1])
    tomato = int(vegs[2])
    total = (carrot * 10) + (cab * 25) + (tomato * 3)
    print(total)
main()
