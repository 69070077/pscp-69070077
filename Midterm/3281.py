"""Ijudge"""
def main():
    """Ijudge"""
    link = input()
    level = 0
    if link[:39] == "https://ijudge.it.kmitl.ac.th/problems/":
        if 42 < len(link) <= 44:
            if link[39:42].isdigit:
                if link[39] == "0":
                    level = "0 STAR"
                elif link[39] == "1":
                    level = "1 STAR"
                elif link[39] == "2":
                    level = "2 STAR"
                elif link[39] == "3":
                    level = "3 STAR"
                else:
                    level = "INVALID"
            else:
                level = "INVALID"
        else:
            level = "INVALID"
    else:
        level = "INVALID"
    print(level)
main()
