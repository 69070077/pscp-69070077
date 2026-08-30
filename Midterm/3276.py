"""Thaiplus"""
def main():
    """Thaiplus"""
    name = input()
    age = int(input())
    income = int(input())
    status = input()
    family = int(input())
    ispass = True
    rank = 0
    getmoney = 0
    if age >= 18:
        if status == "Y":
            rank = "GOLD"
        elif income <= 15000:
            rank = "GOLD"
        elif 15000 < income <= 30000:
            rank = "SILVER"
        else:
            ispass = False
        if family >= 3:
            getmoney += 500
        else:
            getmoney += 0
    else:
        ispass = False
    #เช็คระดับเพื่อเพิ่มเงิน
    if rank == "GOLD":
        getmoney += 3000
    elif rank == "SILVER":
        getmoney += 1500
    if ispass is True:
        print(f"{name} {rank} {getmoney}")
    else:
        print(f"{name} NOT ELIGIBLE")
main()
