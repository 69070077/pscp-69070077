"""GameScoreCal"""
def main():
    """GameScoreCal"""
    score = int(input())
    bonus = int(input())
    days = int(input())
    total_score = score + bonus

    if days > 3:
        total_score = int(total_score * 1.5)
    rank = ""
    if total_score >= 1500:
        rank = "5"
    elif total_score >= 1000:
        rank = "4"
    elif total_score >= 500:
        rank = "3"
    elif total_score >= 200:
        rank = "2"
    elif total_score < 200:
        rank = "1"
    if rank == "5" and days >= 7:
        status = 99
    elif rank == "4" and bonus > 300:
        status = 88
    else:
        status = 0

    print(total_score)
    print(rank)
    print(status)
main()
