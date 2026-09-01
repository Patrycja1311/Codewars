def convert_my_dollars(usd, currency):
    rate = CONVERSION_RATES[currency]
    if currency[0].lower() not in "aeiou":
        rate = int(str(rate), 2)
    return f"You now have {usd * rate} of {currency}."
