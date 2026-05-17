class Class:
    x=1
    @staticmethod
    def get_number():
        val = Class.x
        Class.x *= 2
        return val
