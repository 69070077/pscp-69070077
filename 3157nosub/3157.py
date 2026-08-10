"""Scorecollectgame"""
def main():
    """Scorecollectgame"""
    num = int(input())
    action = []
    for _ in range(num):
        action.append(input())
    symbol = "".join(action)
    plus = (symbol.count('+')) * 10
    minus = (symbol.count('-')) * 5
    score = plus - minus
    print(score)
main()
