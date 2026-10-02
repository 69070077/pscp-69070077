"""Sara"""
def main():
    """sara"""
    text = input().lower()
    total = 0
    if text.count("a"):
        total += text.count("a")
    if text.count("e"):
        total += text.count("e")
    if text.count("i"):
        total += text.count("i")
    if text.count("o"):
        total += text.count("o")
    if text.count("u"):
        total += text.count("u")
    print(total)
main()
