def rpsls(pl1, pl2):
    win = {
        "scissors": {"paper", "lizard"},
        "paper": {"rock", "spock"},
        "rock": {"lizard", "scissors"},
        "lizard": {"spock", "paper"},
        "spock": {"scissors", "rock"}
    }
    return "Draw!" if pl1 == pl2 else "Player 1 Won!" if pl2 in win[pl1] else "Player 2 Won!"
