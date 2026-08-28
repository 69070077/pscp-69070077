"""Teacher"""
def main():
    """Teacher"""
    class_week = int(input())
    time_class = int(input())
    total_min = class_week * time_class
    hour = total_min // 60
    remaintime = total_min % 60
    if not total_min:
        print("No teaching")
    else:
        if total_min < 60:
            print(f"{remaintime} minute")
        elif not remaintime:
            print(f"{hour} hours")
        else:
            print(f"{hour} hours {remaintime} minute")
main()
