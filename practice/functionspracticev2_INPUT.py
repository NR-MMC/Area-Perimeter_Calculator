
#function/s: -----------------------------------------------------------
def makestatement(heading, decoration, lines):
    # a statement for heading text, decorative text that goes around it, and a statement to control the amount of lines produced.


    middle = f"{decoration} {heading} {decoration}"
    top_bottom = decoration * len(middle)

# vvv  printing middle, (the statement + 2 decorations) vvv
    if lines == 1:
        print(middle)

# vvv  printing middle, (the statement + 2 decorations) and 1 decoration line  vvv
    elif lines == 2:
        print(middle)
        print(top_bottom)

# vvv  printing middle, (the statement + 2 decorations) and 2 decoration lines  vvv
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

# ----------------------------------------------------------------------

# asking for the 3 headings, before printing:
quest1 = input("choose your first heading: ")
quest2 = input("choose your second heading: ")
quest3 = input("last one!, choose your third heading: ")

#main routine: ---------------------------------------------------------
print('heres your headings!')
print()
makestatement(quest1, "-", 3)
print()
makestatement(quest2, "/", 3)
print()
makestatement(quest3, "*", 3)
# the amount of lines called for each 'makestatement' controls how many decoration lines are printed next to and around the heading.
# ----------------------------------------------------------------------
