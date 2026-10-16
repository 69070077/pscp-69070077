"""NoxRob"""
def main():
    """Noxrob"""
    n, k = map(int, input().split())

    time = []
    for _ in range(n):
        time.append(int(input()))
    min_s = time[0]
    for t in time:
        if t < min_s:
            min_s = t
    winner_time = k * min_s
    survi = 0
    for t in time:
        if (k - 1) * t < winner_time:
            survi += 1

    print(survi)
main()
