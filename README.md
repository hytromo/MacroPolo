MacroPolo is a python module that can be used in order to automate processes.

While it supports simple mouse movement and key strokes simulation, what really makes MacroPolo different
from other macro operations libraries or programs is that it can powerfully search your screen for pixels.

This means that you can automate many tasks depending on the current color of pixels on your screen. Using
this technic, automating complex processes (like betting at a roulette game, which is not encouraged) becomes
very easy.

# Example usage

~~~ python
#!/usr/bin/env python2

from macropolo import Macro
from time import sleep

# just move the cursor to top left
Macro.move_cursor_to(1, 1)

# write a sentence
sentence = 'You look awesome!'
Macro.keyboard(sentence)

sleep(2)

# delete the sentence
for _ in range(len(sentence)):
    Macro.keyboard(['@@BackSpace'])

sleep(0.1)

# run a command
Macro.keyboard(['ls -al', '@@Return'])
~~~

Most methods are `static`. The only methods that require an instance of `Macro()` are the ones that have to do with pixel searching because they use a specified search speed (like `pixel_color_in_area_counter()` etc)

# Dependencies

Run the following on a debian system to install the dependencies:

~~~ bash
sudo apt-get install python-qt4 python-pyatspi2
~~~

# More info

All the functions inside the module include detailed description of their functionality.

You can access this description either by opening the module file on a text editor and looking at the first
few lines of each function, or through python:

~~~ python
import macropolo
macro = macropolo.Macro()
print macro.middle_click_to.__doc__
~~~

The above outputs:
~~~
'Middle clicks the cursor to the x, y coordinates'
~~~

Module macropolo
----------------

Variables
---------
MOUSE_ABS

app

key_codes

key_list

Functions
---------
to_lower(string)
    Returns python or Qt String to lower

to_upper(string)
    Returns python or Qt String to upper

Classes
-------
Macro 
    Ancestors (in MRO)
    ------------------
    macropolo.Macro

    Static methods
    --------------
    color_of_pixel(x, y)
        Returns the pixel color of the pixel at coordinates x, y.

    get_cursos_pos()
        Returns the cursor pos as a tuple

    key_down(key)
        This is a more specific function than keyboard(). It can send specific
        key-pressed events, in case you want to do keyboard combinations, like Alt+F4
        The argument can only be a string. If you want to send (e.g.) Alt+F4 then you
        should call it as:
        key_down("Alt")
        key_down("F4")
        time.sleep(0.2)
        key_up("Alt")
        key_up("F4")

    key_up(key)
        It releases a pressed key. See the key_down(key) function for more info.

    keyboard(key)
        Types the tuple 'key' to the screen. For example you can say:
        ["Alex was in a bad mood lately", "Return", "A", "B", "1", "2", "comma"] and it will try to print:
        Alex was in a bad mood lately
        AB12,
        A simple string rather than a tuple may as well be passed to this function.

    left_click_to(x, y)
        Left clicks the cursor to the x, y coordinates

    middle_click_to(x, y)
        Middle clicks the cursor to the x, y coordinates

    move_cursor_to(x, y)
        Moves the cursor to the x, y coordinates

    right_click_to(x, y)
        Right clicks the cursor to the x, y coordinates

    save_section_of_the_screen(rectangle, filename)
        Saves the 'rectangle' in 'filename'.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.

    wait_for_no_pixel_color(point, color, timeout)
        Waits till the point 'point' is not of color 'color', checking
        every 'timeout' milliseconds. Then it simply exits.
        point is a tuple [x, y] while color is a string (e.g. #000000)

    wait_for_pixel_color(point, color, timeout)
        Waits till the point 'point' is of color 'color', checking
        every 'timeout' milliseconds. Then it simply exits.
        point is a tuple [x, y]

    wait_for_pixel_colors(points_colors, for_all, timeout)
        'points_colors' argument is a Ax2 array, where A is the number of pixels you want to check.
        For example, the following code:
            points_colors = [ [[5, 6], "#FFFFFF"], [[8, 9], "#000000"] ]
            wait_for_pixel_colors(point_colors, False, 5000)
        will check the pixel 5x6 for the color #FFFFFF and the pixel 8x9 for
        the color #000000 checking every 5 seconds. If one of these colors
        is found then the function exits.
        Note that the pixels are checked one by one in the row they are specified.
        Once all pixels have been checked then the function sleeps for
        'timeout' milliseconds before checking the pixels one by one again. If 'for_all'
        if false, then the function exits if one pixel of all specified has the
        according color, but if 'for_all' is true, then all the specified pixels have to
        have their according color.
        Finally, the function returns the index of the pixel specified. In the above
        example, if the pixel 5x6 has the color #FFFFFF then the function will return
        0, but if the pixel 5x6 doesn't have to color #FFFFFF and the pixel 8x9 has
        the color #000000 then the function will return 1. If there were more pixel-color
        inside the array and e.g. the third pixel-color pair was confirmed, then the function
        would return 2 etc. It is meaningless to return the index if 'for_all' is true, thus
        0 is returned if 'for_all' is true.

    Instance variables
    ------------------
    pixel_search_speed

    Methods
    -------
    __init__(self)

    pixel_color_in_area(self, rectangle, color)
        Searches the rectangle area 'rectangle' for the color 'color'.
        If the 'color' is found inside 'rectangle' then it returns True
        as first argument and the point where the pixel was found as the 2nd argument
        If nothing is found then it simply returns False.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)

    pixel_color_in_area_counter(self, rectangle, color)
        Searches the rectangle area 'rectangle' for the color 'color'.
        It returns an integer indicating the times that the 'color'
        was found inside the 'rectangle'.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)

    setPixelSearchSpeed(self, speed)

    wait_for_no_pixel_color_in_area(self, rectangle, color, timeout)
        Waits till the rectangle 'rectangle' does not contain
        a pixel of color 'color', checking every 'timeout' milliseconds.
        Then it simply exits returning the pixel where the color was found
        first.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)

    wait_for_no_pixel_color_in_area_special(self, function, times, rectangle, color, timeout)
        Waits till the rectangle 'rectangle' does not contain
        a pixel of color 'color', checking every 'timeout' milliseconds.
        It will run the function 'function' when it has checked 'times'
        times for the pixel color (and it hasn't found it, otherwise it exits).
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)

    wait_for_no_pixel_color_special(self, function, times, point, color, timeout)
        Waits till the point 'point' is not of color 'color', checking
        every 'timeout' milliseconds. It will run the function 'function'
        when it has checked 'times' times for the pixel color (and it
        hasn't found it, otherwise it exits).

    wait_for_pixel_color_in_area(self, rectangle, color, timeout)
        Waits till the rectangle 'rectangle' contains a pixel of color
        'color', checking every 'timeout' milliseconds. Then it simply
        exits returning the pixel where the color was found first.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)

    wait_for_pixel_color_in_area_special(self, function, times, rectangle, color, timeout)
        Waits till the rectangle 'rectangle' contains a pixel of color
        'color', checking every 'timeout' milliseconds. It will run the
        function 'function' when it has checked 'times' times for the pixel
        color (and it hasn't found it, otherwise it exits).
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)

    wait_for_pixel_color_special(self, function, times, point, color, timeout)
        Waits till the point 'point' is of color 'color', checking
        every 'timeout' milliseconds. It will run the function 'function'
        when it has checked 'times' times for the pixel color (and it
        hasn't found it, otherwise it exits).
