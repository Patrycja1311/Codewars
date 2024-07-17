def solve(a, b):
    def generate_eviternity_numbers(limit):
        from collections import deque
        eviternity_numbers = []
        queue = deque(['8', '5', '3'])

        while queue:
            num = queue.popleft()
            n = int(num)
            if n > limit:
                continue

            count_8 = num.count('8')
            count_5 = num.count('5')
            count_3 = num.count('3')

            if count_8 >= count_5 >= count_3:
                eviternity_numbers.append(n)

            queue.append(num + '8')
            queue.append(num + '5')
            queue.append(num + '3')

        return eviternity_numbers

    limit = 500000
    eviternity_numbers = generate_eviternity_numbers(limit)
    return sum(a <= num < b for num in eviternity_numbers)
