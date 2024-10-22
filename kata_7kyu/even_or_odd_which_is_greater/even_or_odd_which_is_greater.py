def even_or_odd(s):
    even_sum = sum(int(d) for d in s if int(d) % 2 == 0)
    odd_sum = sum(int(d) for d in s if int(d) % 2)
    return ("Even is greater than Odd" if even_sum > odd_sum else
            "Odd is greater than Even" if odd_sum > even_sum else
            "Even and Odd are the same")
