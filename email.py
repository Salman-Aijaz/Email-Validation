# EMAIL VALIDATION 

# REQUIREMENTS
# a-z
# 0-9
# . _ @ just 1 time
# . will be in 2nd or 3rd position

# ^ start with
# + join 
# \ search 
# ? in regex just appear it just one time if it one or move our condition is false 
import re
email_condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Enter Your E-Mail : ')

if re.search(email_condition,user_email):
    print("Right email")
else:
    print("Wrong Email")    