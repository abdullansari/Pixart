import turtle

"""
This module creates the 20x20 grid for pixel art as well as
color each pixel if prompted to, all using turtle.
"""

PIXEL_SIZE = 30     #Global variable for the pixel's size (length and width).
ROWS = 20           #Global variable for the number of rows the grid will have.
COLUMNS = 20        #Global variable for the number of columns the grid will have.

def initial():
    """
    This function initializes the turtle's pen to be up, speed to be 0
    coordinates to be (-300,300), pen color to be black, and fill color
    to be white.
    """
    turtle.up()
    turtle.speed(0)
    turtle.goto(-300,300)
    turtle.pencolor("Black")
    turtle.fillcolor("White")
    
def draw_pixel(color):
    """
    This function draws a pixel according to the color indicated in the
    function's argument but with a black outline.
    """
    turtle.pencolor("black")
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.down()
    sides = 0
    while sides < 4:        #this loop creates a single square pixel.
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        sides = sides + 1
    turtle.forward(PIXEL_SIZE)
    turtle.end_fill()
    turtle.up()

def draw_row():
    """
    This function uses the draw_pixel() function to draw 20 pixels in series
    (because the global variable ROWS is for 20 pixels) and uses a while loop
    to ensure only 20 are drawn. 
    """
    rowCount = 0
    while rowCount < ROWS:
            draw_pixel("white")     #Fill color is fixed to be white in accordance with the initial() function.
            rowCount = rowCount + 1

def new_row(yCor):
     """
     This function takes turtle to the coordinates of the beginning of the next
     set of pixels (row) and sets its heading to the right (0°).
     """
     turtle.goto(-300,yCor)
     turtle.setheading(0)

def draw_grid():
    """
    This function creates the 20x20 grid using while loop that contains calls to
    the draw_row() and new_row() functions.
    The while loop's condition makes sure that only 20 columns are drawn.
    """
    colCount = 0
    yCor = 300 - PIXEL_SIZE         #y coordinate for the second row of pixels.
    while colCount < COLUMNS: 
        draw_row()
        new_row(yCor)
        yCor = yCor - PIXEL_SIZE    #Sets the new y coordinate for the next set of pixels, each of size 30.
        colCount = colCount + 1

def draw_black_pixel():         #Draws a black pixel by calling the draw_pixel() function.
     draw_pixel("black")

def draw_white_pixel():         #Draws a white pixel by calling the draw_pixel() function.
     draw_pixel("white")

def draw_red_pixel():           #Draws a red pixel by calling the draw_pixel() function.
     draw_pixel("red")

def draw_yellow_pixel():        #Draws a yellow pixel by calling the draw_pixel() function.
     draw_pixel("yellow")

def draw_orange_pixel():        #Draws an orange pixel by calling the draw_pixel() function.
     draw_pixel("orange")

def draw_green_pixel():         #Draws a green pixel by calling the draw_pixel() function.
     draw_pixel("green")

def draw_yellowgreen_pixel():   #Draws a yellow-green pixel by calling the draw_pixel() function.
     draw_pixel("yellowgreen")

def draw_sienna_pixel():        #Draws a sienna pixel by calling the draw_pixel() function.
     draw_pixel("sienna")

def draw_tan_pixel():           #Draws a tan pixel by calling the draw_pixel() function.
     draw_pixel("tan")

def draw_gray_pixel():          #Draws a gray pixel by calling the draw_pixel() function.
     draw_pixel("gray")

def draw_darkgray_pixel():      #Draws a dark gray pixel by calling the draw_pixel() function.
     draw_pixel("darkgray")

def draw_pink_pixel():          #Draws a pink pixel by calling the draw_pixel() function.
    draw_pixel("pink")

def draw_blue_pixel():          #Draws a blue pixel by calling the draw_pixel() function.
    draw_pixel("blue")

def main():       
    initial()
    draw_grid()

if __name__ == "__main__":
    main()