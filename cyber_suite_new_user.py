# FILE NAME: cyber_suite_new_user.py

# NAME: Nate Cancel
# DATE: 02-28-2025
# BRIEF DESCRIPTION: mimick account creation


# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience


# HINT: Tackle this one step at a time. First, just ask the name and the ID number
#       and then print those out. Once you get that working, add in the password.
#
#       Think about how to get the length of the password
#       Then, think about how to print out the Xs. Perhaps you can use string multiplication?

########## ENTER YER CODE BELOW THIS LINE ##########

name = input("Please enter your name: ")
user_id = input("Please enter your user id: ")
password = input("Please enter your password: ")
print()
print(f" Welcome, {name}. Your id is {user_id}. ")
print()

hidden_password = 'X' * len(password)
print(' PASSWORD: ')
print(hidden_password)




########### END YER CODE ABOVE THIS LINE ###########
    

comments - i did have to google the len() function to find a way to mulitply the password into X's

########################################
#          SAMPLE OUTPUT
########################################

'''
Please enter your name: Dave
Please enter your user id: 12345
Please enter your password: abc123

Welcome, Dave. Your ID is 12345.

PASSWORD: 
XXXXXX
'''

'''
Please enter your name: Katie
Please enter your user id: 13090
Please enter your password: PCT2024

Welcome, Katie. Your ID is 13090.

PASSWORD: 
XXXXXXX
'''

'''
Please enter your name: John
Please enter your user id: 10008
Please enter your password: TheOtherDayISawABearAGreatBigBear

Welcome, John. Your ID is 10008.

PASSWORD: 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''
1. This project has a bit of a speed bump (converting the password to XXXXs). What was your thought process?

hardest one to date for sure. print statements are easy now, but the converting the password to X was very hard. 
i had to google how to hide input with X and the len() popped up so i resreached it and it worked perfectly. 



'''
