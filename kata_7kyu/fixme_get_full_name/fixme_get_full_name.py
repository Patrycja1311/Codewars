class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        full_name = ''
        if self.first_name:
            full_name += self.first_name
        if self.last_name:
            if full_name:
                full_name += ' '
            full_name += self.last_name
        return full_name
