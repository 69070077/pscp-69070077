"""PrimeLarge"""
def main():
    """PrimeLarge"""
    num = int(input())
    if num <= 1:
        print("NO")
    else:
        isprime = True
        for i in range(2, int(num**0.5)+1):
            if not num % i:
                isprime = False
                break
        if isprime:
            print("YES")
        else:
            print("NO")
main()
