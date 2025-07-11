from config import PASSWORD_CONFIGS

_use_digits = PASSWORD_CONFIGS.get('use_digits')
_use_lower = PASSWORD_CONFIGS.get('use_lower')
_use_upper = PASSWORD_CONFIGS.get('use_upper')
_use_special = PASSWORD_CONFIGS.get('use_special')
_length = PASSWORD_CONFIGS.get('length')

class PasswordGenerator:
    def __init__(self, digits = _use_digits, lower = _use_lower, upper = _use_upper, special = _use_special, length = _length):
        self.digits = digits
        self.lower = lower
        self.upper = upper
        self.special = special
        self.length = length

        # generating password        
        self.generate()


    def generate(self):
        print(self.digits)
        print(self.lower)
        print(self.upper)
        print(self.special)
        print(self.length)


# 1: init
# 2: generate

p1 = PasswordGenerator()