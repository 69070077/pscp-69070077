"""NotSamePass"""
def main():
    """NotSamePass"""
    _ = input()
    number = list(map(int, input().split()))
    ans = [x for x in number if number.count(x) == 1]
    ans.sort()
    print(" ".join(str(x) for x in ans))
main()
