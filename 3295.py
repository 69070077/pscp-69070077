"""ElectricBill"""
def main():
    """ElectricBill"""
    units = int(input())
    total = 0
    #เเบ่งคิดทีละช่วงของหน่วย
    payunits_1 = min(units, 10)
    total += payunits_1 * 5
    leftunits = units - payunits_1

    payunits_2 = min(leftunits, 40)
    total += payunits_2 * 7
    leftunits = leftunits - payunits_2

    payunits_3 = min(leftunits, 50)
    total += payunits_3 * 10
    leftunits = leftunits - payunits_3

    payunits_4 = min(leftunits, 100)
    total += payunits_4 * 12
    leftunits = leftunits - payunits_4

    total += leftunits*15

    ft = units * 0.50
    vat = total * 0.07
    finaltotal = total + ft + vat
    print(f"{finaltotal:.1f}")

main()
