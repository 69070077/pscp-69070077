"""Saitama"""
def main():
    """Saitama"""
    pushup_need = int(input())
    situp_need = int(input())
    squat_need = int(input())
    run_need = int(input())
    pushup_cando = int(input())
    situp_cando = int(input())
    run_cando = int(input())
    squat_cando = int(input())
    day = []

    daypush = pushup_need // pushup_cando
    if pushup_need % pushup_cando:
        daypush += 1
    day.append(daypush)

    daysitup = situp_need // situp_cando
    if situp_need % situp_cando:
        daysitup += 1
    day.append(daysitup)

    daysquat = squat_need // squat_cando
    if squat_need % squat_cando:
        daysquat += 1
    day.append(daysquat)

    dayrun = run_need // run_cando
    if run_need % run_cando:
        dayrun += 1
    day.append(dayrun)
    print(max(day))
main()
