"""Members"""
def main():
    """Members"""
    teamA = input().split()
    teamB = input().split()
    setA = set(teamA)
    setB = set(teamB)
    onlyA = sorted(list(setA - setB))
    if onlyA :
        print(" ".join(onlyA))
    else:
        print("-")
    totalnotsame = setA | setB
    print(len(totalnotsame))
main()
