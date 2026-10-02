"""Temp"""
def main():
    """Temp"""
    num = int(input())
    strtemp =  input().split()
    temp = []

    for item in strtemp:
        temp.append(int(item))
    totaltemp = sum(temp)
    avgtemp = totaltemp / num
    print(f"{avgtemp:.2f}")

    over = 0
    for t in temp:
        if t > avgtemp:
            over += 1
    print(over)
main()
