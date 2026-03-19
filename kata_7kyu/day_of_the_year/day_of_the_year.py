def to_day_of_year(date):
    d, m, y = date
    days = [31, 28 + (y%4==0 and (y%100!=0 or y%400==0)), 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    return d + sum(days[:m-1])
