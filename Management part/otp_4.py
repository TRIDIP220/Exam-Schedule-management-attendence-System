import os
import math
import random
import smtplib
import webbrowser

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
msg_2 = "file:///C:/Users/Dell/OneDrive/Desktop/testing/index.html"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("kundutridip260@gmail.com", "uwgmbftgrjtzivgq")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)

a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
    webbrowser.open('status.txt')

else:
    print("Please Check your OTP again")