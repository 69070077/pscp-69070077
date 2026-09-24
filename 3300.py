"""Lifebalance"""
def main():
    """Lifebalance"""
    num = int(input())
    lest = [int(input()) for _ in range(num)]
    less = []
    more = []

    for word in lest:
        if word <= 18:
            less.append(word)
        else:
            more.append(word)

    print(num + max(0, len(more) - len(less) - 1))

main()
