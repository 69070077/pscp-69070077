"""faedtech"""
def main():
    """faedtech"""
    num = int(input())
    pass1 = input().strip()
    pass2 = input().strip()
    notmatch = 0
    for i in range(num):
        if int(pass1[i]) + int(pass2[i]) != 9:
            notmatch += 1
    if not notmatch:
        print("YES")
    else:
        print(f"NO {notmatch}")
main()
