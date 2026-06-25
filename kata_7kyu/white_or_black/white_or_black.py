def square_color(file, rank):
    return 'white' if (ord(file)-96+rank) % 2 else 'black'
