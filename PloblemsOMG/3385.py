"""Bus stop"""
def main():
    """Bus lightyear"""
    p = int(input())
    n = int(input())

    st = {}
    for i in range(1, n + 1):
        st[i] = []
    for _ in range(n):
        line = input().split()
        if line:
            stop_num = int(line[0])
            desk = [int(x) for x in line[1:]]
            st[stop_num] = desk

    bus = []
    kon = 0
    for cur in range(1, n + 1):
        rem = []
        for d in bus:
            if d == cur:
                kon += 1
            else:
                rem.append(d)
        bus = rem
        for d in st[cur]:
            if d > cur and len(bus) < p:
                bus.append(d)
    print(kon)
main()
