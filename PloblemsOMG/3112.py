"""MilkTea"""
bubble = input().split()#              เจอวิธีที่สั้นกว่าเเต่ไหนๆก็มาขนาดนี้ ผมขี้เกียจจะทำใหม่
bubble_type = bubble[0]
bubble_vol = float(bubble[1])
tea = input().split()
tea_type = tea[0]
sweet = tea[1]
tea_vol = int(tea[2])
honeycal = bubble_vol * 5
originalcal = bubble_vol * 3
jellycal = bubble_vol * 2
if tea_type == 'R':
    if sweet == '1':
        teacal = tea_vol * 12
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
    elif sweet == '2':
        teacal = tea_vol * 18
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
    elif sweet == '3':
        teacal = tea_vol * 25
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
elif tea_type == 'T':
    if sweet == '1':
        teacal = tea_vol * 15
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
    elif sweet == '2':
        teacal = tea_vol * 20
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
    elif sweet == '3':
        teacal = tea_vol * 30
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
elif tea_type == 'M':
    if sweet == '1':
        teacal = tea_vol * 10
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
    elif sweet == '2':
        teacal = tea_vol * 15
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
    elif sweet == '3':
        teacal = tea_vol * 20
        if bubble_type == 'H':
            caltotal = teacal + honeycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'O':
            caltotal = teacal + originalcal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
        elif bubble_type == 'J':
            caltotal = teacal + jellycal
            if caltotal.is_integer():
                print(int(caltotal))
            else:
                print(caltotal)
