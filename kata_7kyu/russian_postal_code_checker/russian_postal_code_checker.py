def zipvalidate(postcode):
    return (
        isinstance(postcode, str)
        and len(postcode) == 6
        and postcode.isdigit()
        and postcode[0] not in "05789"
    )
