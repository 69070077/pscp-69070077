"""FrogJump"""
def main():
    """FrogJump"""
    x, y = map(int, input().split())
    dis = 0
    jump = 0
    while dis < y:
        if x <= 0:
            jump = -1
            break
        dis += x
        jump += 1
        x -= 2
    print(jump)
main()
