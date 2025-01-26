import random 
import string

pas_len = 8

charValues = string.ascii_letters + string.digits + string.punctuation


password = "".join([random.choice(charValues) for i in range(pas_len)])


print("Your random password is: ",  password)