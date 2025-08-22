
# heading function: ----------------------------------------------------
def makestatement(heading, decoration):
    wrappingdeco = decoration * len(heading)
    print(wrappingdeco)
    print(heading)
    print(wrappingdeco)

# ----------------------------------------------------------------------

# intro prompt function:
def yes_no(question):
    """checks that users enter yes / y or no / n"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print(instructions)
            return

        elif response == "no" or response == "n":
            return

        else: #repeats question
            print("please give a valid response \n")


instructions = " [to be written] "



#main routine: ---------------------------------------------------------
makestatement("Nate’s Area/Perimeter Calculator", "=")
print()
instructprompt = yes_no("want the instructions? (Y/N)  ")

# ----------------------------------------------------------------------
