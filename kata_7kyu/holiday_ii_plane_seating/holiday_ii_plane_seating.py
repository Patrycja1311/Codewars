def plane_seat(seat: str) -> str:
    if len(seat) < 2:
        return "No Seat!!"

    number_part = "".join(filter(str.isdigit, seat))
    letter_part = "".join(filter(str.isalpha, seat))

    if not number_part.isdigit() or not letter_part:
        return "No Seat!!"

    seat_number = int(number_part)
    seat_letter = letter_part.upper()

    valid_letters = "ABCDEFGHK"
    if seat_number < 1 or seat_number > 60 or seat_letter not in valid_letters:
        return "No Seat!!"

    if 1 <= seat_number <= 20:
        section = "Front"
    elif 21 <= seat_number <= 40:
        section = "Middle"
    else:
        section = "Back"

    if seat_letter in "ABC":
        position = "Left"
    elif seat_letter in "DEF":
        position = "Middle"
    else:
        position = "Right"

    return f"{section}-{position}"