"""Delivery"""
def main():
    """Delivery"""
    wheretowhere = input()
    weight = float(input())
    wheretowhere = wheretowhere.split(" ")
    place_1st = wheretowhere[0]
    place_2nd = wheretowhere[1]
    startprice = 0.00

    if place_1st == 'BKK' and place_2nd == 'CNX':
        startprice = 10.00
        price_per_weight = weight * 30
        total_price = price_per_weight + startprice
        print(f"{total_price:.2f}")
    elif place_1st == 'CNX' and place_2nd == 'UBP':
        startprice = 15.00
        price_per_weight = weight * 40
        total_price = price_per_weight + startprice
        print(f"{total_price:.2f}")
    elif place_1st == 'UBP' and place_2nd == 'BKK':
        startprice = 20.00
        price_per_weight = weight * 40
        total_price = price_per_weight + startprice
        print(f"{total_price:.2f}")
    elif place_1st == 'BKK' and place_2nd == 'PKT':
        startprice = 25.00
        price_per_weight = weight * 50
        total_price = price_per_weight + startprice
        print(f"{total_price:.2f}")
    elif place_1st == 'PKT' and place_2nd == 'CNX':
        startprice = 30.00
        price_per_weight = weight * 60
        total_price = price_per_weight + startprice
        print(f"{total_price:.2f}")
    elif place_1st == 'UBP' and place_2nd == 'PKT':
        startprice = 40.00
        price_per_weight = weight * 70
        total_price = price_per_weight + startprice
        print(f"{total_price:.2f}")
    else:
        print("Error")
main()
