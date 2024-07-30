Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... import string
... 
... def generate_password(length=12):
...     characters = string.ascii_letters + string.digits + string.punctuation
...     password = ''.join(random.choice(characters) for i in range(length))
...     return password
... 
... # Example usage
... password = generate_password()
