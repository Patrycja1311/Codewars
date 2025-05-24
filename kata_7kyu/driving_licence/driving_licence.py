from datetime import datetime


def driver(data):
    first_name, middle_name, surname, dob, gender = data
    surname_part = surname.upper().ljust(5, '9')[:5]
    try:
        dob_obj = datetime.strptime(dob, "%d-%b-%Y")
    except ValueError:
        dob_obj = datetime.strptime(dob, "%d-%B-%Y")
    year = dob_obj.year
    month = dob_obj.month
    day = dob_obj.day
    decade_digit = str(year)[2]
    if gender.upper() == "F":
        month += 50
    month_str = f"{month:02d}"
    day_str = f"{day:02d}"
    year_digit = str(year)[3]
    initials = first_name[0].upper()
    initials += middle_name[0].upper() if middle_name else '9'
    arbitrary = '9'
    check = 'AA'
    license_number = (
        surname_part +
        decade_digit +
        month_str +
        day_str +
        year_digit +
        initials +
        arbitrary +
        check
    )
    return license_number

