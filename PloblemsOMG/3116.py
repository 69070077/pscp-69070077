"""InnovationOfSchool"""
def main():
    """InnovationOfSchool"""
    name_school = input()
    num = len(name_school)
    ascii_first = ord(name_school[0].upper())
    ascii_last = ord(name_school[-1].upper())
    password = []
    for pos in range(1, 11):
        val = pos - 1
        if pos % 2:
            code = ascii_first + val
        else:
            code = ascii_last - val
        rem = code % num
        if rem > 9:
            rem = rem % 10
        password.append(rem)
    ans = password[2:8]
    print(*ans)
main()
