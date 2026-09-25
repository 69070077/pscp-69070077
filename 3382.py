"""Backward"""
def main():
    """Backward"""
    obj = []
    while True:
        word = input()
        if not word == "NULL":
            obj.append(word)
        else:
            break
    obj.reverse()
    for text in obj:
        print(text)
main()
