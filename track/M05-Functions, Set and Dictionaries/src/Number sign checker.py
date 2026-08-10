def check_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    pass

number = int(input())
print(check_sign(number))




#can write as this
# print(check_sign(int(input())))       #this will give output in single line

#summary: using function we can call the function n number of times with different inputs
#using if-elif-else we can check the sign of the number