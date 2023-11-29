def how_much_i_love_you(nb_petals):
    dic_petal = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return dic_petal[(nb_petals % 6) - 1]
