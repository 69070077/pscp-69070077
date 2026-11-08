"""Members"""
def main():
    """Members"""
    while True:
        num = int(input())
        time = 1
        if not num:
            break
        while num > 1:
            if not num % 2:
                num = num // 2
            else:
                num = (num * 3) + 1
            time += 1
        print(time)
main()
