import pixart

"""
This module creates and draws pixel art according to the user's input.
It imports pixart and utilizes its functions and global variable PIXEL_SIZE
"""

def drawings_initial():
    """
    This function initializes turtle the same way as in
    the pixart module's initialize function.
    """
    pixart.initial()

def color_pixel(charString):
    """
    This function takes a string of characters and uses
    a for loop to go over each character.
    If the selected character is equal to a color's character
    then it draws a pixel of that color using the draw_...._color()
    function from the pixart module.
    If all characters in the inputted string are valid then the
    function returns true, otherwise it returns false.
    """
    for x in charString:
        if x == "0":
            pixart.draw_black_pixel()
        elif x == "1":
            pixart.draw_white_pixel()
        elif x == "2":
            pixart.draw_red_pixel()
        elif x == "3":
            pixart.draw_yellow_pixel()
        elif x == "4":
            pixart.draw_orange_pixel()
        elif x == "5":
            pixart.draw_green_pixel()
        elif x == "6":
            pixart.draw_yellowgreen_pixel()
        elif x == "7":
            pixart.draw_sienna_pixel()
        elif x == "8":
            pixart.draw_tan_pixel()
        elif x == "9":
            pixart.draw_gray_pixel()
        elif x == "A":
            pixart.draw_darkgray_pixel()
        elif x == "B":
            pixart.draw_pink_pixel()
        elif x == "C":
            pixart.draw_blue_pixel()
        else: 
            return False
    return True

def color_strings():
    """
    This function takes the user's inputted string and then calls
    the color_pixel() function to draw it accordingly.
    It prompts the user to keep inputting a string using a while loop
    until an invalid character or string is inputted, then the function
    stops.
    """
    yCor = 300 - pixart.PIXEL_SIZE #y coordinate for the next row of pixels. 
    while True:
        colorStrings = input("Enter your color strings: ")
        c = color_pixel(colorStrings)
        if c == False:
            break
        else:
            pixart.new_row(yCor)
            yCor = yCor - pixart.PIXEL_SIZE #Sets new y coordinate for the next row of pixels after each iteration.

def main():
    drawings_initial()
    color_strings()

if __name__ == "__main__":
    main()