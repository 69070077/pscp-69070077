"""ScoreTest"""
def main():
    """ScoreTest"""
    score_1 = int(input())
    score_2 = int(input())
    score_3 = int(input())

    if score_1 >= 5 and score_2 >= 20 and score_3 >= 25 :
        print("pass")
    elif score_1 < 5 or score_2 < 20 or score_3 <25:
        print("fail")
main()
