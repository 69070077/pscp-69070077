"""Bookname"""
def main():
    """Bookname"""
    my_dict = {}
    while True:
        text = input()
        if text == "END":
            break
        key, value = text.split()
        if key not in my_dict:
            my_dict[key] = [value]
        else:
            if value not in my_dict[key]:
                my_dict[key].append(value)
    if not my_dict:
        print("No Information")
    else:
        for name, book in my_dict.items():
            print(f"{name}: {book}")
main()
