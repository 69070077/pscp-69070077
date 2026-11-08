"""BookWorm"""
def main():
    """BookWorm"""
    total_test = int(input())
    for _ in range(total_test):
        total_time = float(input())
        book = int(input())

        time_per_book = []
        for _ in range(book):
            time_per_book.append(float(input()))
        time_per_book.sort()

        read_book = 0
        current_time = 0
        for i in time_per_book:
            if current_time + i <= total_time:
                current_time += i
                read_book += 1
            else:
                break
        print(read_book)
main()
