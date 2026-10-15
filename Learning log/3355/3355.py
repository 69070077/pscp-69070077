"""shorten"""
def main():
    """shorten"""
    number = []
    while True:
        num = int(input())
        if num == -1:
            break
        number.append(num)
    if not number:
        print("")
    else:
        numlist = []
        start = number[0]
        now = number[0]
        for num in number[1:]:
            if num == now + 1:
                now = num
            else:
                if start == now:
                    numlist.append(str(start))
                else:
                    numlist.append(f"{start}-{now}")
                start = num
                now = num
        if start == now:
            numlist.append(str(start))
        else:
            numlist.append(f"{start}-{now}")
        print(", ".join(numlist))
main()
