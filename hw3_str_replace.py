"""
# HW 3 - String Replacements

## Description

For this assignment, modify the function "str_replace" to prompt the user for
the following string:

- A message
- A substring to replace
- A substring to replace with

Using the first string, replace all instances of the second string with the
value of the third string.  Print out the resulting string.

### Example usage

>>> python3 hw3_str_replace.py
Please enter a message or phrase:
You do talk about fight club
Please enter the substring(s) you wish to replace:
do
Please enter the substring you wish to replace it with:
don't
Your replaced message is: "You don't talk about fight club"

## Instructions

Replace/alter the contents between the START and END comments below with your
code to fulfill this assignemnt.

### Requirements
- You *must* use `input` to prompt the user for string values.
"""

def str_replace():
    # START: your code here
    str_replace = input("Please enter a message or phrase: ")
    print(str_replace)
    word_error = input("Please enther the substring you wish to replace: ")
    print(word_error)
    word_replace = input("please enther the substring you wish to replace it with: ")
    print(word_replace)
    new_message = str_replace.replace(word_error, word_replace)
    print(new_message)
    # END: your code here

if __name__ == "__main__":
    str_replace()

