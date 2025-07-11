from config import PASSWORD_CONFIGS
from string import digits, ascii_lowercase, ascii_uppercase

# Defining config variables
_use_digits = PASSWORD_CONFIGS.get('use_digits')
_use_lower = PASSWORD_CONFIGS.get('use_lower')
_use_upper = PASSWORD_CONFIGS.get('use_upper')
_use_special = PASSWORD_CONFIGS.get('use_special')
_length = PASSWORD_CONFIGS.get('length')

# Software core class
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
        # Phase 1: generating character sets

        # Character sets list
        character_sets = []

        # a dictionary with all instance variables and their values
        variables = vars(self)

        # Extracting password length from instance variables
        password_length = variables.pop('length')

        # Generating sets
        for key, value in variables.items():
            # Checking if included
            if value:
                match key:
                    # Generating digits set if included
                    case 'digits':
                        character_sets.append(list(digits))
                    
                    # Generating lower-case set if included
                    case 'lower':
                        character_sets.append(list(ascii_lowercase))
                    
                    # Generating upper-case set if included
                    case 'upper':
                        character_sets.append(list(ascii_uppercase))
                    
                    # Generating special set if included
                    case 'special':
                        character_sets.append(list('!@#$%^&*()-_=+'))
        
        # Deleting instance variables dictionary for memory management
        del variables


p1 = PasswordGenerator()