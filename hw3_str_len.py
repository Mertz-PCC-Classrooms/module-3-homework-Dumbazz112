"""
# HW 3 - String Length

## Description

For this assignment, modify the function "str_len" to use `input` to prompt the
user for a string statement.  You will then print the length of the string to
the user.

### Example usage

>>> python3 hw3_str_len.py
Please enter your string:
This is the way
Your string is 15 characters long!

## Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

### Requirements
- You *must* use `input` to prompt the user for the string value.
"""

def str_len():
    # START: your code here
    str_len = input("Please enter your string: ")
    print(str_len)
    message_length = len(str_len)
    #print(length)
    print("Your sting is " + str(message_length) + " characters long!")
    # END: your code here

if __name__ == "__main__":
    str_len()
