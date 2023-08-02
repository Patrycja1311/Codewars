def convert(number):
    nums = [int(number[i:i+2]) for i in range(0, len(number), 2)]
    output_str = ''.join(chr(num) if 65 <= num <= 90 else ' ' for num in nums)
    return output_str
