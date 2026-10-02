"""CatinBag"""
def main():
    """catinBag"""
    cat = 0
    bag = []
    while True:
        word = input().lower()
        if word == "-1":
            break
        if "cat" in  word:
            cat += 1
            bag.append(word)
    print(f"The number of cat in bag {cat}")
    print(f"List of cat {bag}")
main()
