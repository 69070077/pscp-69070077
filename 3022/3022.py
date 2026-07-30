"""Temperature"""
def main():
    """Temperature"""
    temp = float(input())
    temp_unit = input()
    temp_trans = input()
#เเปลงหน่วยอุณหภูมิ input to C
    temp_total = 0.0
    if temp_unit == 'C':
        temp_total = temp
    elif temp_unit == 'K':
        temp_total = temp - 273.15
    elif temp_unit == 'F':
        temp_total = 5 / 9 * (temp - 32)
    elif temp_unit == 'R':
        temp_total = (temp * 5 / 9) - 273.15
#เเปลงหน่วยอุณหภูมิ C to temp_trans
    temp_ans = 0.0
    if temp_trans == 'C':
        temp_ans = temp_total
    elif temp_trans == 'K':
        temp_ans = temp_total + 273.15
    elif temp_trans == 'F':
        temp_ans = temp_total * 9 / 5 + 32
    elif temp_trans == 'R':
        temp_ans = (temp_total + 273.15) * 9 / 5

    print(f"{temp_ans:.2f}")
main()
