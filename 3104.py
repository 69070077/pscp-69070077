"""3104"""
text = input()
text_split = text.split(" ")
age = int(text_split[0])
day = text_split[1]
if 0 <= age < 5:
    print("0")
elif 5 <= age <= 18:
    if day == 'Wed':
        print("50")
    else:
        print("100")
elif 19 <= age <= 120:
    if day == 'Wed':
        print("75")
    else:
        print("150")
