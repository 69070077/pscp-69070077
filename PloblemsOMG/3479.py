"""NameOFCard"""
def main():
    """namofooocard"""
    card = input().strip().upper()
    point = card[:-1]
    symbol = card[-1]

    point_ajqk = {
        "A": "Ace",
        "J": "Jack",
        "Q": "Queen",
        "K": "King"
    }
    symbol_type = {
        "D": "Diamonds",
        "H": "Hearts",
        "S": "Spades",
        "C": "Clubs"
    }
    point_name = point_ajqk.get(point, point)
    print(f"{point_name} of {symbol_type[symbol]}")

main()
