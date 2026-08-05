"""A,B"""
def main():
    """A,B"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())
    total = 0
    for i in range(A , B+1):
        if i % d == r:
            total += 1
    print(total)
main()
