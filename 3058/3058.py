"""BrickBridge"""
def main():
    """BrickBridge"""
    smallbrick = int(input())
    bigbrick = int(input())
    goal = int(input())
    bigbrick = bigbrick * 5
    goal = abs(goal - bigbrick)
    if smallbrick <= goal :
        print(goal)
    else:
        print("-1")
main()
