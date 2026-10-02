"""Laststand"""
import json
def main():
    """Laststand"""
    text = input()
    word = json.loads(text)
    for i in word:
        i = str(i)
        print(i[-1])
main()
