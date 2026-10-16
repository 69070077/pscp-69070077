"""GetinLine"""
def main():
    """Getinline"""
    num = int(input().split()[0])
    height = list(map(int, input().split()))
    customers = list(map(int, input().split()))
    max_before = [0] * num
    cur_max = 0

    for i in range(num):
        max_before[i] = cur_max
        if height[i] > cur_max:
            cur_max = height[i]

    for idx in customers:
        position = idx - 1
        m = max_before[position]
        need = (m + 1) - height[position]
        if need < 0:
            need = 0
        print(need)
main()
