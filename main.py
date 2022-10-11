# from checker import checkLength
#
# pwd = "test"
#
# if(checkLength(pwd, 3)):
#     print("hello world")


import string
import secrets
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(20))

print(password)
