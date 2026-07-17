"""Calculator"""
def main():
    """Calculator"""
    n = int(input())
    x = 0
    if n == 1 :
        print("1")
    else :
        for i in range(1, n+1):
            x += (len(str(i))) + 1
        print(x)
main()
