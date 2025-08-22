#functions:
def yes_no(question):
    """checks that users enter yes / y or no / n"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "thats a yes"

        elif response == "no" or response == "n":
            return "thats a no"

        else:
            print("please give a valid response \n")
            return response

# ------------------------------------------------------------------------------

# main routine
# 'while True' is being used to create a loop for testing purposes.
while True:
    instructprompt = yes_no("want the instructions? ")
    print(f"{instructprompt} to printing the instructions. \n")