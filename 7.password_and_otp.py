import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}[]._.!@#$"

all = lower + upper + numbers + symbols

length = 5
password = "".join(random.sample(all,length))
print("Generated Password: " + password)



#another method to generate password using secrets module
import secrets

password = secrets.token_urlsafe()
print("Generated Password: " + password)



#generate otp using secrets module 
import secrets

otp = f"{secrets.randbelow(1_000_000):06d}"
print("OTP:" + otp)