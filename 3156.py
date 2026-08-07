"""Conan"""
def main():
    """Conan"""
    text = input()
    num = int(input())
    result = ""
    for i in text:
        asciii = chr((ord(i) - 97 + num)% 26 + 97 )
        ressult += asciii
    print(result)
main()
