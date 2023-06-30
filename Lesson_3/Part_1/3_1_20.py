from datetime import date

def get_min_max(list_of_dates):
    if not list_of_dates:
        return ()
    return (min(list_of_dates), max(list_of_dates))