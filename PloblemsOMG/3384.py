"""Pickthem"""
import json
def main():
    """Pickthem"""
    text = input()
    word = json.loads(text)
    odd = []
    for i in word:
        if not i % 2:
            odd.append(i)
    if not odd:
        print("Nope")
    else:
        for i in odd:
            print(i)
main()
