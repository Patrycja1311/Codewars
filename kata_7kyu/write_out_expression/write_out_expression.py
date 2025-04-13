def expression_out(exp):
    ops = {
        "+": "Plus", "-": "Minus", "*": "Times", "/": "Divided By",
        "**": "To The Power Of", "=": "Equals", "!=": "Does Not Equal"
    }
    nums = {str(i): w for i, w in enumerate(
        ["Zero", "One", "Two", "Three", "Four", "Five",
         "Six", "Seven", "Eight", "Nine", "Ten"]
    )}
    a, op, b = exp.split()
    return f"{nums[a]} {ops[op]} {nums[b]}" if op in ops else "That's not an operator!"
