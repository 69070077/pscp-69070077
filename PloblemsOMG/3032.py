"""RabbitScore"""
def main():
    """RabbitScore"""
    rabbit = int(input())
    scoretotal = []
    i = 0
    while i < rabbit :
        scoretotal.append(int(input()))
        i += 1

    print(max(scoretotal))
    maxscore = max(scoretotal)
    scorecount = scoretotal.count(maxscore)
    print(scorecount)
main()
