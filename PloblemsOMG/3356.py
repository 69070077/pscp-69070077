"""BusSeat"""
def main():
    """BusSeat"""
    seat_row = int(input())
    num_row = int(input())
    target_seat = int(input())
    for i in range(seat_row, 0, -1):
        rowlist = []
        for t in range(1, num_row + 1):
            seat_num = i + ((t - 1) * seat_row)
            if seat_num == target_seat:
                rowlist.append("XX")
            else:
                rowlist.append(f"{seat_num:02d}")
        print(" ".join(rowlist))

        if i % 2 and i > 1:
            print()
main()
