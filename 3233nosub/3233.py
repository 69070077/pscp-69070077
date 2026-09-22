"""Lottery"""
def main():
    """Lottery"""
    win_text, win_num = input().split()
    me_text, me_num = input().split()

    is_textmatch = win_text == me_text
    is_allnum_match = win_num == me_num
    is_last2num = win_num[-2:] == me_num[-2:]
    is_last3num = win_num[-3:] == me_num[-3:]

    if is_textmatch and is_allnum_match:
        getprize = 1000000
    elif is_allnum_match:
        getprize = 100000
    elif is_textmatch and is_last3num:
        getprize = 2000
    elif is_textmatch and is_last2num:
        getprize = 1000
    elif is_last3num:
        getprize = 200
    elif is_last2num:
        getprize = 100
    elif is_textmatch:
        getprize = 20
    else:
        getprize = 0
    print(getprize)
main()
