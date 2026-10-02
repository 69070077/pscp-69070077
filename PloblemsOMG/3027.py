"""Rabbit2"""
def main():
    """Rabbit2"""
    num = input()
    price = int(input())
    num_split = num.split(" ")
    width = int(num_split[0])
    long = int(num_split[1])
    floor = int(num_split[2])
    sq = ((width + long) * 2 ) * floor
    total = sq * price
    print(sq)
    print(total)
main()
