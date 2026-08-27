"""Airport"""
import math
time_in = input().strip()
time_out = input().strip()
in_hour, out_minute = map(int, time_in.split('.'))
out_h, out_m = map(int, time_out.split('.'))

if not ( 0 <= in_hour <= 23 and 0 <= out_minute <= 59
        and 0 <= out_h <= 23 and 0 <= out_m <= 59
):
    print("ERROR")
else:
    in_total_m = in_hour * 60 + out_minute
    out_total_m = out_h * 60 + out_m
    if out_total_m < in_total_m:
        print("ERROR")
    else:
        diff_m = out_total_m - in_total_m
        if diff_m > 24 * 60:
            print("ERROR")
        elif diff_m <= 15:
            print("FREE")
        else:
            hour = math.ceil(diff_m / 60)
            if hour == 1:
                print(25)
            elif hour == 2:
                print(50)
            elif hour == 3:
                print(80)
            elif hour == 4:
                print(110)
            elif hour == 5:
                print(145)
            elif hour == 6:
                print(180)
            elif 7 <= hour <= 24:
                print(250)
            else:
                print("ERROR")
