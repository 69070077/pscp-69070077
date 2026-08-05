"""Gift Paper"""
def main():
    """Gift Paper"""
    rgift, hgift, lgift = map(float, input().split())
    PI = 3.14
    width = hgift + (2 * rgift)
    length = (2 * PI * rgift) + lgift
    print(f"{width:.2f} {length:.2f}")
main()
