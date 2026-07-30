def box_capacity(length, width, height):
    crate_size = 16 / 12

    return (
        int(length // crate_size)
        * int(width // crate_size)
        * int(height // crate_size)
    )

