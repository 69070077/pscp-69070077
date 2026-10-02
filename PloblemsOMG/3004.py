"""3D"""
def main():
    """3D"""
    text = input()
    text_s = text.split(" ")
    x1 = int(text_s[0])
    y1 = int(text_s[1])
    z1 = int(text_s[2])
    text2 = input()
    text2_s = text2.split(" ")
    x2 = int(text2_s[0])
    y2 = int(text2_s[1])
    z2 = int(text2_s[2])
    d = (((x1 - x2)**2) + ((y1 - y2)**2) + ((z1 - z2)**2))**0.5
    print(f"{d:.2f}")
main()
