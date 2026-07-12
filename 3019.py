"""Safe"""
def main():
    """Safe"""
    text = input()
    num = int(input())
    password = text + str(num)
    print(password)
    if password == 'H4567':
        print("safe unlocked")
    elif not password == '4567':
        print("safe locked - change digit")
    elif password == 'h4567':
        print("safe locked - change char")
    else:
        print("sefe locked")
    
main()
