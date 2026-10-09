"""SumOfNum"""
def main():
    """SumOfNum"""
    num_target = int(input())
    total = 0
    while True:
        num = int(input())
        if num == -1:
            break
        total += num
        if total == num_target:
            break
    print(total)
main()
