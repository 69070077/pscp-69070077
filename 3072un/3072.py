"""Detect sara"""
def main():
    """Detect sara"""
    aeiou = input().lower()
    if aeiou.count("a") > 0:
        print(f"a : {aeiou.count("a")}")
    if aeiou.count("e") > 0:
        print(f"e : {aeiou.count("e")}")
    if aeiou.count("i") > 0:
        print(f"i : {aeiou.count("i")}")
    if aeiou.count("o") > 0:
        print(f"o : {aeiou.count("o")}")
    if aeiou.count("u") > 0:
        print(f"u : {aeiou.count("u")}")
main()
