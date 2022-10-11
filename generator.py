import string
import secrets

# Constantes
MIN_LENGTH = 12
DEFAULT_COMPLEXITY = 3
DEFAULT_NUMBER_PASSWORD_CREATION = 5

class Generator:

    def __init__(self):
        # Complexity of password:
        # 1 => letter only
        # 2 => letter + number
        # 3 => letter + number + punctuation
        # Default: max complexity (3)
        self.complexity = DEFAULT_COMPLEXITY

        # Length of Password
        # Default: minimum
        self.length = MIN_LENGTH

        # Number of password generated per try
        # Default: 5
        self.nbrOfPwd = DEFAULT_NUMBER_PASSWORD_CREATION


    # All function permite to change parameter of generator
    def setComplexity(self, data):
        self.complexity = data

    def setLength(self, data):
        self.length = data

    def setNbr(self, data):
        self.nbrOfPwd = data

    # Creation of password
    def create(self):
        # Complexity of password:
        # 1 => letter only
        # 2 => letter + number
        # 3 => letter + number + punctuation
        if self.complexity == 1:
            alphabet = string.ascii_letters
        elif self.complexity == 2:
            alphabet = string.ascii_letters + string.digits
        else:
            alphabet = string.ascii_letters + string.digits + string.punctuation

        # Creating x password
        for i in range(self.nbrOfPwd):
            pwd = ''.join(secrets.choice(alphabet) for i in range(self.length))
            print(pwd)
