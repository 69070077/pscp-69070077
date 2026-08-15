'''กระต่ายอ้วนตัวอ้วน'''
def main():
    '''กระต่ายอ้วนตัวอ้วน'''
    bunny = int(input())
    i = 0
    maxw = 0
    maxn = 0
    for _ in range(bunny):
        name, weight = input().split()
        weight = int(weight)
        if weight > 15:
            i += 1
        if weight > maxw:
            maxw = weight
            maxn = name

    print(i)
    print(maxn)
main()
