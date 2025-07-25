import random
import string

passwordLength = 12  # Default password length
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [function(i) for i in range(n)]
res = "".join([random.choice(charValues) for _ in range(passwordLength)])
print("Generated Password:", res)


# password = ""
# for i in range(passwordLength):
#  password += random.choice(charValues)

# print("Generated Password:", password)
# print("Password Length:", passwordLength)

# This code generates a random password of a specified length using letters, digits, and punctuation.
# You can change the passwordLength variable to generate a password of a different length. 

