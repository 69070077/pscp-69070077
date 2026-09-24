"""bigframe"""
def main():
    """bigframe"""
    word = [input() for _ in range(5)]
    long = max(len(w) for w in word)
    print("*" * (long + 4))
    for i in word:
        print(f"* {i:<{long}} *")
    print("*" * (long + 4))
main()
