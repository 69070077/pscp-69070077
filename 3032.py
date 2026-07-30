"""RabbitScore"""
def main():
    """RabbitScore"""
    rabbit = int(input())
    scoretotal = []    
    i = 0
    while i < rabbit :
        scoretotal.append(int(input()))
        i += 1
    scoresort = str(scoretotal.sort())
    print(scoresort[0::-1])
    lenscore = len(str(min(scoretotal)))
    print(scoretotal)
    print(lenscore)
main()
