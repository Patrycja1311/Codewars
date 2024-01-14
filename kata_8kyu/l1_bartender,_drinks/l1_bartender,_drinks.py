def get_drink_by_profession(param):
    dict_word = {"Jabroni": "Patron Tequila", "School Counselor": "Anything with Alcohol", "Programmer": "Hipster Craft Beer", "Bike Gang Member": "Moonshine", "Politician": "Your tax dollars", "Rapper": "Cristal"}
    param_1 = ' '.join(param.title().split())
    return dict_word.get(param_1, "Beer")
