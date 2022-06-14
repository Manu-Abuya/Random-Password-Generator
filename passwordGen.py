import random
import string

# Ask user to enter a length of password
length = int(input('\nEnter the length of password: '))

# Define the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# This line randomly selects one character from
# all the characters defined
all = lower + upper + num + symbols

# Characters are joined together
temp = random.sample(all, length)
password = "".join(temp)

all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all, length))

print(password)
