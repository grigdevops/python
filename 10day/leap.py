def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_f, month_f):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_f > 12 or month_f < 1:
        return "Invalid month entered"
    if is_leap(year_f) and month_f == 2:
            leap_num = month_days[1]+1
            days_month = leap_num
    else:
            days_month = month_days[month_f - 1]


    return days_month



year = int(input("Enter a year: "))
month = int(input("Enter a Month "))
days = days_in_month(year, month)

print(days)