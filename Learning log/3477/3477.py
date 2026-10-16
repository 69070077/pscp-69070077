"""PadThai"""
def main():
    """PadThai"""
    word = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts",
    }
    used = []

    while True:
        text = input()
        if text == "Cook":
            break
        used.append(text)
    taste = []
    while True:
        text = input()
        if text == "End":
            break
        taste.append(text)
    if any(text not in word for text in used):
        print("This is not Pad Thai!!!")
    elif set(used) != word:
        print("This is bad!")
    elif set(taste) == {"Sweet", "Sour", "Salty"}:
        print("Delicious!")
    else:
        print("Not Bad...")
main()
