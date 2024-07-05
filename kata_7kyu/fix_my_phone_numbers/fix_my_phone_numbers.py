import re


def is_it_a_num(s: str) -> str:
    cleaned_number = re.sub(r'\D', '', s)
    if len(cleaned_number) == 11 and cleaned_number.startswith('0'):
        return cleaned_number
    else:
        return "Not a phone number"
