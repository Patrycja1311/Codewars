def valid_parentheses(paren_str):
    balance = 0
    for char in paren_str:
        balance += 1 if char == '(' else -1
        if balance < 0:
            return False
    return balance == 0
