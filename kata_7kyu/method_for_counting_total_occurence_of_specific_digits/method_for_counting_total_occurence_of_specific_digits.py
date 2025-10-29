class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        return [(d, ''.join(str(abs(n)) for n in integers_list).count(str(d))) for d in digits_list]
