"""Rec Triangel"""
def main():
    """Rec Triangel"""
    num = int(input())
    for row in range(num):
        for col in range(row +1):
            if not col or row == col or row == num-1:
                print("0", end="")
            else:
                print("1", end="")
        print()
main()
