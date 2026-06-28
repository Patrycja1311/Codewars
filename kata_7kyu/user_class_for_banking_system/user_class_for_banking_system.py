class User:
    def __init__(s, name, balance, checking_account):
        s.name, s.balance, s.checking_account = name, balance, checking_account

    def withdraw(s, a):
        if s.balance < a: raise ValueError
        s.balance -= a
        return f"{s.name} has {s.balance}."

    def check(s, i, a):
        if not i.checking_account or i.balance < a: raise ValueError
        i.balance -= a
        s.balance += a
        return f"{s.name} has {s.balance} and {i.name} has {i.balance}."

    def add_cash(s, a):
        s.balance += a
        return f"{s.name} has {s.balance}."
