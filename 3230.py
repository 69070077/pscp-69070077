"""Hotel13"""
num = input()
n1 = int(num[0])
n2 = int(num[1])
n3 = int(num[2])
n4 = int(num[3])
n5 = int(num[4])
if n1 > 5:
    FIRST = "9"
elif n2 > 5:
    FIRST = "10"
elif n3 > 5:
    FIRST = "11"
elif n4 > 5:
    FIRST = "12"
elif n5 > 5:
    FIRST = "14"
else:
    FIRST = "13"

if num == num[::-1]:
    if n1 + n5 > 5:
        SECOND = "1"
    elif n2 * n4 > 5:
        SECOND = "2"
    else:
        SECOND = "0"
else:
    if n5 and n1 // n5 > 5:
        SECOND = "1"
    elif n2 - n5 > 5:
        SECOND = "2"
    else:
        SECOND = "0"

if n1 + n2 + n3 + n4 + n5 > 25:
    THIRD = "1"
elif n1 * n2 * n3 * n4 * n5 > 55:
    THIRD = "2"
else:
    THIRD = "0"

print(FIRST + SECOND + THIRD)
