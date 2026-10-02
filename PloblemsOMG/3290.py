"""leftArrow"""
def main():
    """LeftArrow"""
    lenght = int(input())
    height = int(input())
    mid =  height // 2
    for i in range(height):
        space = abs(i - mid)
        print(" " * space + "*" * lenght)
main()
