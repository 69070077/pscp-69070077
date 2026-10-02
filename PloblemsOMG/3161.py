"""symbol"""
def main():
    """symbol"""
    num = int(input())
    i = 0
    for i in range(0,num):
        i += 1
        if i % 5:
            print("*", end="")
        elif not i % 5:
            print("X", end="")
main()
