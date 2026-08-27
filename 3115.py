"""Arcade of Time"""
def main():
    """Arcade of Time"""
    num,_ = map(int,input().split())
    open_store = [0] * 1441
    for _ in range(num):
        start, stop = map(int, input().split())
        for minute in range(start, stop):
            open_store[minute] += 1
    check_time = list(map(int, input().split()))
    results = []
    for k in check_time:
        results.append(open_store[k])
    print(*results)
main()
