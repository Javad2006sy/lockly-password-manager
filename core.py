from config import PASSWORD_CONFIGS as cg

class PasswordGenerator:
    def __init__(self, use_digits = cg.get('use_digits'), use_lower = cg.get('use_lower'), use_upper = cg.get('use_upper'), use_special = cg.get('use_special'), length = cg.get('length')):
        self.use_digits = use_digits
        self.use_lower = use_lower
        self.use_upper = use_upper
        self.use_special = use_special
        self.length = length

        # generating password
        self.generate()


    def generate(self):
        print(self.use_digits)
        print(self.use_lower)
        print(self.use_upper)
        print(self.use_special)
        print(self.length)


# 1: init
# 2: generate

p1 = PasswordGenerator()