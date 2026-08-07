"""walkinfestival"""
def main():
    """walkinfestival"""
    text = input()
    x = 0
    y = 0
    lentext = len(text)
    for i in range(lentext):
        if text.count('N') > 0:
            y += 1
        if text.count('S') > 0:
            y -= 1
        if text.count('E') > 0:
            x += 1
        if text.count('W') > 0:
            x -= 1
    d = abs(x + y)
    print(x, y, d)
main()
