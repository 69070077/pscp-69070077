"""Coke"""
def main():
    """Coke"""
    a = int(input())#เดิมราคาขวด
    b = int(input())#จำนวน b ฝา
    c = int(input())#ขวดใหม่ราคา
    d = int(input())#ต้องการ Coke จำนวน
    if not d:
        print(0)
    elif not b or c == a:
        print(d * a)
    else:
        x = (d - 1) // b
        re = d - (x*b)
        cost = ((b - 1) *a ) + c
        total = (x * cost) + (re * a)
        print(total)
main()
