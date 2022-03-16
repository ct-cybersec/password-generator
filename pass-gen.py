#very simple python script to print out a random string of 16 characters for a password
import random
import string

letters = string.ascii_letters
numbers = string.digits
punctuation = "$!&%@"
together = letters + numbers + punctuation

print(''.join(random.choices(together,k=16)))