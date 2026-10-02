"""PickThemAgain"""
def main():
    """PickThemAgain"""
    num = input().split()
    result = []
    for i in num:
        if not int(i) % 3 or not int(i) % 5:
            result.append(i)
    if not result:
        print("Nope")
    else:
        for item in reversed(result):
            print(item)
main()
