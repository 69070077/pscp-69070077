"""LukTaoO"""
def main():
    """LuktaoO"""
    player = int(input())
    banker = int(input())
    if not 1 <= player <= 6 or not 1 <= banker <= 6:
        print("Invalid")
    elif 1 <= player <= 6 and 1 <= banker <= 6:
        if player == banker:
            print("Correct!")
        else:
            print("Wrong!")
main()
