"""bowl"""
def main():
    """bowl"""
    num = int(input())
    counts = {}

    for _ in range(num):
        size = input()
        if size in counts:
            counts[size] += 1
        else:
            counts[size] = 1

    print(max(counts.values()))
main()
