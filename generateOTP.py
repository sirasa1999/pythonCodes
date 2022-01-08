import random,math

n=int(input("Enter no. of digits for OTP: "))
def generateOTP():
    OTP=""
    for i in range(n):
        a=random.random()
        b=math.floor(a*10)
        OTP+= str(b)
    return OTP

print("The ",n,"digit OTP is= ", generateOTP())