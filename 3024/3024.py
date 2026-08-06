"""Surprising"""
def main():
    """Surprising"""
    total_score = float(input())
    max_score = float(input())
    min_score = max(0, (total_score - max_score) - max_score)
    if max_score - 2 > min_score:
        print("Surprising")
    else:
        print("Not surprising")
main()
