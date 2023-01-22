import random
import string
import sys
import os

try:
	password = int(sys.argv[1])
except TypeError:
	print("\033[1;38;2;255;110;110mDon't be silly, it has to be an integer 🤦\033[0m\n\033[1mExample usage: python pass-gen.py 10\033[0m")
	sys.exit(1)
except IndexError:
	print("\033[1;38;2;255;110;110mDon't be silly, input something at least 🤦\033[0m\n\033[1mExample usage: python pass-gen.py 10\033[0m")
	sys.exit(1)
except ValueError:
	print("\033[1;38;2;255;110;110mDon't be silly, it has to be an integer 🤦\033[0m\n\033[1mExample usage: python pass-gen.py 10\033[0m")
	sys.exit(1)

if password >= 1:
	if (password <= 50) & (password >= 6):
	    password_length = password
	    letters = string.ascii_letters
	    numbers = string.digits
	    punctuation = "$!&%@.,#?"
	    together = letters + numbers + punctuation
	    print("\033[1;38;2;100;201;135m" + "".join(random.choices(together,k=password_length)))
	if password > 50:
		print("\033[1;38;2;255;110;110mPlease provide a reasonable password length (i.e. 6-50)\033[0m 🤦")
	if password < 6:
		print("\033[1;38;2;255;110;110mCome on, you shouldn't be using a password that's less than 6... try again\033[0m 🤦")
else:
	print("\033[1;38;2;255;110;110mPlease try again by providing an integer value. Run the program as such:\033[0m\n\033[1mpython pass-gen.py 10\033[0m")


