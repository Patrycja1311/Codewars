def rake_garden(garden):
    items = garden.split()
    cleaned_garden = ['gravel' if item != 'rock' else item for item in items]
    return ' '.join(cleaned_garden)
