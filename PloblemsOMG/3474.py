"""Resistor"""
def main():
    """Resistor"""
    num = {
        "Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
        "Green": 5, "Blue": 6, "Purple": 7, "Grey": 8, "White": 9,
    }
    multi = {
        "Black": 1, "Brown": 10, "Red": 100, "Orange": 1000,
        "Yellow": 10000, "Green": 100000, "Blue": 1000000,
        "Purple": 10000000, "Gold": 0.1, "Silver": 0.01,
    }
    tol = {
        "Brown": 1, "Red": 2, "Green": 0.5, "Blue": 0.25,
        "Purple": 0.10, "Grey": 0.05, "Gold": 5, "Silver": 10,
    }

    color1 = input().strip()
    color2 = input().strip()
    color3 = input().strip()
    color4 = input().strip()

    if color1 not in num or color2 not in num or color3 not in multi or color4 not in tol:
        print("Error")
        return
    value = (num[color1] * 10 + num[color2]) * multi[color3]

    p = tol[color4]
    low = value * (1 - p / 100)
    high = value * (1 + p / 100)
    print(f"{low:.4f}")
    print(f"{high:.4f}")
main()
