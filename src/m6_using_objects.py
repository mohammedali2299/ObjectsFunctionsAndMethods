"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and mohammed.
"""  # TOdoneDO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():

    two_circles()
    circle_and_rectangle()
    lines()





    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():
    """


    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.

    """
    window = rg.RoseWindow(1000,1000)

    point1 = rg.Point(300,200)
    point1.attach_to(window)

    point2 = rg.Point(300,150)
    point2.attach_to(window)

    circle1 = rg.Circle(point1,90)
    circle1.attach_to(window)

    circle2 = rg.Circle(point2,100)
    circle2.attach_to(window)

    circle1.fill_color = 'blue'
    window.render(1)
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # TOdoneDO: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window2 = rg.RoseWindow(1000,1000)



    point3 = rg.Point(300, 200)
    point3.attach_to(window2)
    point4 = rg.Point(400, 300)
    harry = rg.Circle(point3,80)
    harry.fill_color = 'blue'
    harry.attach_to(window2)
    potter = rg.Rectangle(point3, point4)
    potter.attach_to(window2)
    print(harry.outline_thickness)
    print(harry.fill_color)
    print(harry.center)
    print(300)
    print(200)
    print(potter.outline_thickness)
    print(potter.fill_color)
    print(potter.get_center())
    print(350)
    print(250)
    window2.render(1)



    window2.close_on_mouse_click()







    # ------------------------------------------------------------------
    # TODdoneO: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------

    window3 = rg.RoseWindow()
    point5 = rg.Point(100,100)
    point6 = rg.Point(200,100)
    point7 = rg.Point(100,200)
    line1 = rg.Line(point5 ,point6)
    line1.thickness = 5
    line2 = rg.Line(point5, point7)
    line1.attach_to(window3)
    line2.attach_to(window3)

    print(line1.get_midpoint())
    print(150)
    print(100)

    window3.render()
    window3.close_on_mouse_click()
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
