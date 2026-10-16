"""Buppea"""
a = input().strip()
b = input().strip()

i = 0
while len(a) < len(b):
    a += a[i]
    i += 1
i = 0
while len(b) < len(a):
    b += b[i]
    i += 1
r = ""
w_count = 0

for i in range(len(a)):
    c1 = a[i].lower()
    c2 = b[i].lower()
    if c1 in "love" or c2 in "love":
        r += "w"
        w_count += 1
    else:
        r += "$"

if w_count % 2:
    max_con = 0
    cur_con = 0
    for char in r:
        if char == "w":
            cur_con += 1
            if cur_con > max_con:
                max_con = cur_con
        else:
            cur_con = 0
    r += str(max_con)
else:
    has_con = False
    for i in range(len(r) - 1):
        if r[i] == "w" and r[i + 1] == "w":
            has_con = True
            break
    if not has_con:
        r += "#"
print(r)
