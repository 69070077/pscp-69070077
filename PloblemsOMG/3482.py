"""DemonSlayer"""
def main():
    """เบียวเเตก"""
    queue = [
        ("Spider Demon", 1),
        ("Swamp Demon", 2),
        ("Arrow Demon", 1),
        ("Hand Demon", 2),
        ("Drum Demon", 3),
        ("Mugen Train", 2),
        ("Upper Moon", 3)
    ]
    kill = 0
    total_atk = 0

    while kill < 5:
        name, correct = queue.pop(0)
        print(name)
        att = 0
        passed = False
        while att < 2:
            try:
                value = int(input().strip())
            except EOFError:
                break
            total_atk += 1
            att += 1
            if value == correct:
                print("kill")
                kill += 1
                passed = True
                break
        if passed:
            if kill == 5:
                break
        else:
            print("back")
            queue.append((name, correct))
    print(total_atk)
main()
