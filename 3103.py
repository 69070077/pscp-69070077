"""TotalSara"""
def main():
    """TotalSara"""
    num = int(input())
    text = []
    n = 0
    i = 0
    i -= 1
    for i in range(num):
        text.append(input())
    word = "".join(text)
    if word.count('A'):
        n += 1
    if word.count('E'):
        n += 1
    if word.count('I'):
        n += 1
    if word.count('O'):
        n += 1
    if word.count('U'):
        n += 1
    print(n)
main()
