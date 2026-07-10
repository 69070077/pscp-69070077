"""color"""
def main():
    """color"""
    firstcolor = input()
    secondcolor = input()
    if firstcolor == 'Red' and secondcolor == 'Yellow':
        print("Orange")
    elif firstcolor == 'Blue' and secondcolor == 'Red':
        print("Violet")
    elif firstcolor == 'Yellow' and secondcolor == 'Blue':
        print("Green")
    elif firstcolor == 'Red'and secondcolor == 'Blue':
        print("Violet")
    elif firstcolor == 'Blue' and secondcolor == 'Yellow':
        print("Green")
    elif firstcolor == 'Yellow' and secondcolor == 'Red':
        print("Orange")
    elif firstcolor == 'Red' and secondcolor == 'Red':
        print("Red")
    elif firstcolor == 'Blue' and secondcolor == 'Blue':
        print("Blue")
    elif firstcolor == 'Yellow' and secondcolor == 'Yellow':
        print("Yellow")
    else:
        print("Error")
main()
