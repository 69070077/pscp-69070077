"""Zodiac"""
day = int(input())
month = int(input())
if month == 12 :
    if 22 <= day <= 31:
        print("capricorn")
    elif 1 <= day <= 21:
        print("sagittarius")
if month == 1:
    if 1 <= day <= 19:
        print("capricorn")
    elif 20 <= day <= 31:
        print("aquarius	")
if month == 2:
    if 1 <= day <= 18:
        print("aquarius")
    elif 19 <= day <= 29:
        print("pisces")
if month == 3:
    if 1 <= day <= 20:
        print("pisces")
    elif 21 <= day <= 31:
        print("aries")
if month == 4:
    if 1 <= day <= 19:
        print("aries")
    elif 20 <= day <= 30:
        print("taurus")
if month == 5:
    if 1 <= day <= 20:
        print("taurus")
    elif 21 <= day <= 31:
        print("gemini")
if month == 6:
    if 1 <= day <= 21:
        print("gemini")
    elif 22 <= day <= 30:
        print("cancer")
if month == 7:
    if 1 <= day <= 22:
        print("cancer")
    elif 23 <= day <= 31:
        print("leo")
if month == 8:
    if 1 <= day <= 22:
        print("leo")
    elif 23 <= day <= 31:
        print("virgo")
if month == 9:
    if 1 <= day <= 22:
        print("virgo")
    elif 23 <= day <= 30:
        print("libra")
if month == 10:
    if 1 <= day <= 23:
        print("libra")
    elif 24 <= day <= 31:
        print("scorpio")
if month == 11:
    if 1 <= day <= 21:
        print("scorpio")
    elif 22 <= day <= 30:
        print("sagittarius")
