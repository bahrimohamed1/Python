def cc(days):
    if days > 1:
        days -= 1
        cc(days)
        print(f"Day {days}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    cc(days + 1)
    print("Harvest time!")
