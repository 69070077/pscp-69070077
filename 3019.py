"""Safe"""
def main():
    """Safe"""
    text = input()
    num = int(input())
    num2 = str(num)
    if text == 'H' and num2 == '4567':
        print("safe unlocked")
    elif text == 'H' and num2 != '4567':
        print("safe locked - change digit")
    elif text == 'h' and num2 == '4567':
        print("safe locked - change char")
    elif text != 'H' and num2 == '4567':
        print("safe locked - change char")
    else:
        print("safe locked")
main()
