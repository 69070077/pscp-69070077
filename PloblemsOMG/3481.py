"""SaPaan"""
def main():
    """PaanSa"""
    num = int(input().split()[1])

    sapaan = []
    for _ in range(num):
        a, b = map(int, input().split())
        sapaan.append((a, b))
    max_sapaan = 0

    for a, b in sapaan:
        x = a + 0.5
        count = 0
        for start, end in sapaan:
            if start < x < end:
                count += 1
        if count > max_sapaan:
            max_sapaan = count
    print(max_sapaan)
main()
