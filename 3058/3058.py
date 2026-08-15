"""BrickBridge"""
def main():
    """BrickBridge"""
    smallbrick = int(input())
    bigbrick = int(input())
    goal = int(input())

    use_big = min(bigbrick, goal // 5)
    remaining_length = goal - (use_big * 5)

    if smallbrick >= remaining_length:
        print(remaining_length)
    else:
        print(-1)
main()
