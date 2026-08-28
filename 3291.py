"""RightArrow"""
def main():
    """RightArrow"""
    lenght = int(input())
    height = int(input())
    mid =  height // 2
    for i in range(height):
        space = mid - abs(i - mid)
        print(" " * space + "*" * lenght)
main()
