"""Same"""
def main():
    """Same"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 == num2 == num3:
        print("all the same")
    elif num1 == num2 and num1 != num3:
        print("neither")
    elif num1 == num3 and num1 != num2:
        print("neither")
    elif num2 == num3 and num2 != num1:
        print("neither")
    elif num1 != num2 != num3:
        print("all different")
main()
