"""Bonus"""
def main():
    """Bonus"""
    job = input()
    jobsplit = job.split()
    job_title = str(jobsplit[0]).upper()
    year = int(jobsplit[1])
    money = int(jobsplit[2])
    bonus = 0
    if job_title == 'M':
        bonus += 1500
        if year <= 5:
            bonus_percent = money * 0.06
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
        elif 5 < year <= 10:
            bonus_percent = money * 0.08
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
        elif year > 10:
            bonus_percent = money * 0.1
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
    elif job_title == 'B':
        bonus += 1000
        if year <= 5:
            bonus_percent = money * 0.05
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
        elif 5 < year <= 10:
            bonus_percent = money * 0.06
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
        elif year > 10:
            bonus_percent = money * 0.07
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
    elif job_title == 'G':
        bonus += 500
        if year <= 5:
            bonus_percent = money * 0.04
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
        elif 5 < year <= 10:
            bonus_percent = money * 0.05
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
        elif year > 10:
            bonus_percent = money * 0.06
            total_bonus = bonus + bonus_percent
            print(int(total_bonus))
main()
