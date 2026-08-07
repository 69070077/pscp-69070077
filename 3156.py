"""Conan"""
def main():
    """Conan"""
    text = input()
    num = int(input())
    for i in text:
        ascii = ord(i)
        ascii += num
        print(chr(ascii), end="")