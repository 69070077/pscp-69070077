"""Sign"""
def main():
    """Sign"""
    size = int(input())
    position = input()
    text = input()
    space = size - len(text)

    if position == "center":
        rspace = space // 2
        lspace = space - rspace
        print((" " * lspace) + text + (" " * rspace))
    elif position == "right":
        print((" " * space) + text)
    elif position == "left":
        print(text + (" " * space))
main()
