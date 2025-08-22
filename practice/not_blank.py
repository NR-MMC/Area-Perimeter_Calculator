# a script that gets input from a user, and checks that the response is not blank.

# ------------------------------------------------------------------------------------------------------------------

def not_blank(question):
    """checks that a user response isnt blank"""
# triple quotes gives a description for a function """ """


    while True:
        response = input(question)

        if response != "":
            return response
# In Python, != is the "not equal to" operator
# 'return [variable]' finishes the process, and returns back to the start of that process.


        print("your response cant be blank! \n")
# \n moves the next print to a new line.

# ------------------------------------------------------------------------------------------------------------------

# main routine

who = not_blank("please enter your name: ")
print(f"whats up {who}!")