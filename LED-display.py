digits = (
    ("  #", "###", "###", "# #", "###", "###", "###", "###", "###", "###"),
    ("  #", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #", "# #"),
    ("  #", "###", "###", "###", "###", "###", "  #", "###", "###", "# #"),
    ("  #", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #", "# #"),
    ("  #", "###", "###", "  #", "###", "###", "  #", "###", "###", "###")
    )

def display_digit(digit):                   # function to display single digit in cmd-line
    for row in range(5):                    # simply print the ASCII-graphics row-by-row
        print(digits[row][digit])           # "digits" tuple was designed for easy access
    print()                                 # add a blank line at the bottom for prettiness


def display_integer(inp):                   # function to display multiple digits in cmd-line
    for row in range(5):                    # simply print the ASCII-graphics row-by-row
        for ch in inp:                      # for every digit in user input
            print(digits[row][int(ch)-1], end=" ") # query the "digits" tuple for graphics
        print()                             # carret return -> next row
    print()                                 # add a blank line at the bottom for prettiness
        
####    Main    ####
while True:
    to_display = input("Enter any non-negative integer (or type q to quit): ")
    # if the input is ok -> display that integer
    if to_display.isdigit():
        display_integer(to_display)
    # if user wants to quit -> terminate the program
    elif to_display == "q":
        break
    # if the input is bad -> try again
    else:
        print("Some error in input. Only numbers are allowed.")


