
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


#main routine: ---------------------------------------------------------
makestatement("hi im the first heading", "-", 3)
print()
makestatement("hi im the second heading", "/", 3)
print()
makestatement("hi im the third heading", "*", 3)
# the amount of lines called for each 'makestatement' controls how many decoration lines are printed next to and around the heading.
# ----------------------------------------------------------------------
