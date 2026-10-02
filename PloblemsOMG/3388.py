"""113"""
def main():
    """113"""
    text = input()
    stack = []
    for char in text:
        stack.append(char)
        if len(stack) >= 3 and stack[-3] == "1" and stack[-2] == "1" and stack[-1] == "3":
            stack.pop()
            stack.pop()
            stack.pop()
    print("".join(stack))
main()
