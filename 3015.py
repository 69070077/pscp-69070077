"""Pro"""
def main():
    """Pro"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input()) #คนที่มา
    pro = z//x  #จำนวนโปรที่ใช้
    if x >= y :
        free = pro * (x-y) #คนที่ฟรี
        total = (z - free)*a
        print(total)
main()
