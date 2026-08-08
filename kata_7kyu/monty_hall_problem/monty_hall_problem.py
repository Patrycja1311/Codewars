def monty_hall(correct_door_number, participant_guesses):
    wins = sum(guess != correct_door_number for guess in participant_guesses)
    return round(wins * 100 / len(participant_guesses))

