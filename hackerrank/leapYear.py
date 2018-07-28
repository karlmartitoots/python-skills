def is_leap(year):
    if not year%400:
        return True
    if not year%100:
        return False
    return False if year%4 else True