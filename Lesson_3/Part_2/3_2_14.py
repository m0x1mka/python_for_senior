from datetime import date


def print_good_dates(dates):
    dates.sort()
    for i in dates:
        if i.strftime("%Y") == "1992":
            if int(i.strftime("%m")) + int(i.strftime("%d")) == 29:
                print(i.strftime("%B %d, %Y"))
