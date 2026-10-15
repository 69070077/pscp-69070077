"""Card 44"""
def main():
    """Card 44"""
    card = input().strip().upper()
    point = card[:-1]
    symbol = card[-1]

    point_ajqk = {
        "A": "ace",
        "J": "jack",
        "Q": "queen",
        "K": "king"
    }
    symbol_type = {
        "D": "diamonds",
        "H": "hearts",
        "S": "spades",
        "C": "clubs"
    }
    point_name = point_ajqk.get(point, point)
    print(f"{point_name} of {symbol_type[symbol]}")

main()
