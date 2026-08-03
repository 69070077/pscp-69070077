"""Airport"""
def main():
    """Airport"""
    time_in = float(input())
    time_out =  float(input())
    time_total = time_out - time_in
    if time_total <= 0.15:#ฟรี
        print("FREE")
    elif 0.15 < time_total <= 1.00:#ชั่วโมงเเรก
        print("25")
    elif 1.00 < time_total <= 2.00:#ชั่วโมงสอง
        print("50")
    elif 2.00 < time_total <= 3.00:#ชั่วโมงสาม
        print("80")
    elif 3.00 < time_total <= 4.00:#ชั่วโมงสี่
        print("110")
    elif 4.00 < time_total <= 5.00:#ชั่วโมงห้า
        print("145")
    elif 5.00 < time_total <= 6.00:#ชั่วโมงหก
        print("180")
    else:
        print("250")
main()
