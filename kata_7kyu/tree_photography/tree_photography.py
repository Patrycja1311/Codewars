def tree_photography(lst):
    def visible(arr):
        m = c = 0
        for x in arr:
            if x > m:
                c += 1
                m = x
        return c
    return "left" if visible(lst) > visible(lst[::-1]) else "right"
