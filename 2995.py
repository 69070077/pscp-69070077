"""NUM"""
def main():
    """NUM"""
    idtag = input()
    m = len(idtag)
    if m == 8:
        if idtag[2] == '1' and idtag[3] == '6':
            print("yes")
        else:
            print("no")
    else:
        print("no")
main()
