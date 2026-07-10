"""Bill"""
def main():
    """Bill"""
    m = int(input())
    ser = m * 0.1
    if ser < 50:
        ser = 50
    elif ser > 1000:
        ser = 1000
    vat = (m + ser) * 0.07
    total = m + ser + vat
    print(f"{total:.2f}")
main()
