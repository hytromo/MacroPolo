#!/usr/bin/env python
import gi
gi.require_version('Atspi', '2.0')

from gi.repository import Atspi
from pyatspi import Registry as controller
from pyatspi import (KEY_SYM, KEY_PRESS, KEY_PRESSRELEASE, KEY_RELEASE, MOUSE_ABS)
from PyQt4.QtGui import QPixmap, QApplication, QColor, QImage, QDesktopWidget, QCursor
from PyQt4.QtCore import QPoint, QRect
import sys, time

def to_upper(string):
    """
    > Description
        Returns python or Qt string to uppercase

    > Paremeters
        string: the string to convert to uppercase
    
    > Returns
        string (str): the uppercase string without changing the initial type (QString or python string)

    > Example
        # typical python string
        name = 'alex'
        print to_upper('alex') # ALEX (as python string)

        # QString
        name = QtCore.QString('alex')
        print to_upper('alex') # ALEX (as QString)
    """
    try:
        return string.toUpper()
    except:
        return string.upper()


def to_lower(string):
    """Returns python or Qt String to lower"""
    try:
        return string.toLower()
    except:
        return string.lower()

def needQApp(func):
    def wrapper(*args, **kwargs):
        MacroClass = args[0]
        if (MacroClass.APP is None):
            # need to create a QApplication
            MacroClass.APP = QApplication(sys.argv)
        return func(*args, **kwargs)
    return wrapper

class Macro:
    APP = None # QApplication will be constructed only if needed
    KEY_LIST = {
            "1":10, "2":11, "3":12, "4":13, "5":14, "6":15, "7":16, "8":17, "9":18, "0":19, "-":20, "=":21, "`":49, ".":60, "Esc":9, "Shift":50, "Win":133, "Up":111, "Down":116, "Left":113, "Right":114, "Ctrl":37, "Alt":64, "space":65, " ":65, "Return":36, "A":38, "B":56, "C":54, "D":40, "E":26, "F":41, "G":42, "H":43, "I":31, "J":44, "K":45, "L":46, "M":58, "N":57, "O":32, "P":33, "Q":24, "R":27, "S":39, "T":28, "U":30, "V":55, "W":25, "X":53, "Y":29, "Z":52, "a":38, "b":56, "c":54, "d":40, "e":26, "f":41, "g":42, "h":43, "i":31, "j":44, "k":45, "l":46, "m":58, "n":57, "o":32, "p":33, "q":24, "r":27, "s":39, "t":28, "u":30, "v":55, "w":25, "x":53, "y":29, "z":52, "F1":67, "F2":68, "F3":69, "F4":70, "F5":71, "F6":72, "F7":73, "F8":74, "F9":75, "F10":76, "F11":95, "F12":96, "BackSpace":22
    }

    SHIFT_KEY_LIST = {
        "!": KEY_LIST["1"],
        "@": KEY_LIST["2"],
        "#": KEY_LIST["3"],
        "$": KEY_LIST["4"],
        "%": KEY_LIST["5"],
        "^": KEY_LIST["6"],
        "&": KEY_LIST["7"],
        "*": KEY_LIST["8"],
        "(": KEY_LIST["9"],
        ")": KEY_LIST["0"],
        "_": KEY_LIST["-"],
        "+": KEY_LIST["="]
    }

    def __init__(self):
        self.pixel_search_speed=1;

    def set_pixel_search_speed(self, speed):
        """
        > Description
            Set the search speed (aka the number of pixels to skip forward on each iteration) for functions that search for pixel colors in areas of the screen.

            Use this method when the searched color is known to be present on continuous areas of the screen, so as to speed up the search operation.

            Use with caution when the searched color is present in areas with width smaller than the pixel search speed.

            The default value of the pixel search speed is 1

        > Parameters
            speed (int): the number of pixels to add to the current pixel while searching. E.g. if speed is 3 then after reading pixel #1 it will skip to pixel #1+3 = #4, skipping 2 pixels

        > Returns
            None

        > Example
            m = new Macro()

            # set the pixel search speed to 3
            m.set_pixel_search_speed(3)

            # now search in the rectangle [100, 200, 500, 500] for a green pixel, skipping 2 pixels each time (searching only 1/3 of the pixels)
            found, point = m.pixel_color_in_area([100, 200, 500, 500], '#00ff00')
        """
        self.pixel_search_speed=speed;

    @staticmethod
    def move_cursor_to(x, y):
        """
        > Description
            Moves the cursor to the x, y coordinates

        > Parameters
            x (int): the x coordinate to move the cursor to
            y (int): the y coordinate to move the cursor to

        > Returns
            None

        > Example
            # move the cursor to 100, 100
            Macro.move_cursor_to(100, 100)
        """
        controller.generateMouseEvent(x, y, MOUSE_ABS)
    
    @classmethod
    @needQApp
    def get_cursor_pos(cls):
        """
        > Description
            Get the current cursor position

        > Parameters
            None

        > Returns
            cursor_pos (list): a point containing the x and y coordinates of the current pixel position

        > Example
            # get the current cursor position
            cur_pos = Macro.get_cursor_pos()

            # move the cursor 100 pixels to the right
            Macro.move_cursor_to(cur_pos[0] + 100, cur_pos[1])
        """
        return [QCursor.pos().x(), QCursor.pos().y()]

    @staticmethod
    def mouse_event(x, y, button, eventType):
        """
        > Description
            Generates a mouse press or release event on a specific pixel on the screen

        > Parameters
            x (int): the x coordinate where the event will be generated
            y (int): the y coordinate where the event will be generated
            button (str): A string indicating which mouse button to press/release. One of 'left', 'right' or 'middle'
            eventType (str): A string indicating the event type. One of 'press' or 'release'

        > Returns
            None

        > Example
            # this example could demonstrate a drag and drop of a file

            # press the left mouse button at 100, 100
            Macro.mouse_event(100, 100, 'left', 'press')
            # move the cursor to 400, 400
            Macro.move_cursor_to(400, 400)
            # then, release the mouse
            Macro.mouse_event(400, 400, 'left', 'press')
        """
        buttonToNo = {'left':1, 'right':2, 'middle':3 }
        controller.generateMouseEvent(x, y, 'b' + str(buttonToNo[button]) + ('p' if eventType == 'press' else 'r'))

    @staticmethod
    def left_click_to(x, y):
        """
        > Description
            Left clicks the mouse at x, y

        > Parameters
            x (int): the x coordinate to left click to
            y (int): the y coordinate to left click to

        > Returns
            None

        > Example
            # left click to 100, 100
            Macro.left_click_to(100, 100)
        """
        if(x >= 0 and y >= 0):
            controller.generateMouseEvent(x, y, 'b1c')
            
    @staticmethod
    def middle_click_to(x, y):
        """
        > Description
            Middle clicks the mouse at x, y

        > Parameters
            x (int): the x coordinate to middle click to
            y (int): the y coordinate to middle click to

        > Returns
            None

        > Example
            # middle click to 100, 100
            Macro.middle_click_to(100, 100)
        """
        if(x >= 0 and y >= 0):
            controller.generateMouseEvent(x, y, 'b2c')
            
    @staticmethod
    def right_click_to(x, y):
        """
        > Description
            Right clicks the mouse at x, y

        > Parameters
            x (int): the x coordinate to right click to
            y (int): the y coordinate to right click to

        > Returns
            None

        > Example
            # right click to 100, 100
            Macro.right_click_to(100, 100)
        """
        if(x >= 0 and y >= 0):
            controller.generateMouseEvent(x, y, 'b3c')
    
    @staticmethod
    def __generate(i):
        inShiftKeyList = i in Macro.SHIFT_KEY_LIST
        if not (i in Macro.KEY_LIST or inShiftKeyList):
            print 'Cannot type the character \'' + i +'\''

        needShift = inShiftKeyList or i.isupper()

        if needShift:
            controller.generateKeyboardEvent(Macro.KEY_LIST['Shift'], None, KEY_PRESS)

        controller.generateKeyboardEvent((Macro.SHIFT_KEY_LIST if inShiftKeyList else Macro.KEY_LIST)[i], None, KEY_PRESS)
        time.sleep(0.01)
        controller.generateKeyboardEvent((Macro.SHIFT_KEY_LIST if inShiftKeyList else Macro.KEY_LIST)[i], None, KEY_RELEASE)

        if needShift:
            controller.generateKeyboardEvent(Macro.KEY_LIST['Shift'], None, KEY_RELEASE)

    @staticmethod
    def keyboard(key):
        """
        > Description
            Type some text or special keys, like Backspaces, Returns etc

            For all the available keys look into `Macro.KEY_LIST`

        > Parameters
            key (string/list): If the `key` is a string, then it is simpy typed out. If it is a list of strings, every string in the list will be typed out. If a string in the list starts with `@@` then it is recognized as a special key and it is not typed out as is

        > Returns
            None

        > Example
            sentence = 'alex is awesome'

            # types out 'alex is awesome'
            Macro.keyboard(sentence)

            # types out '@@BackSpace'
            Macro.keyboard('@@BackSpace')

            # sends a backspace (deletes a character)
            Macro.keyboard(['@@BackSpace'])

            # types out 'alex is awesome' and then proceeds to go to the next line
            Macro.keyboard([sentence, '@@Return'])
        """
        if type(key) is str:
            for i in key:
               Macro. __generate(i)
        elif type(key) in [tuple, list]:
            for inner_str in key:
                if inner_str.startswith('@@'):
                    inner_str = inner_str[2:]
                    if inner_str in Macro.KEY_LIST:
                        controller.generateKeyboardEvent(Macro.KEY_LIST[inner_str], None, KEY_PRESS)
                        time.sleep(0.01)
                        controller.generateKeyboardEvent(Macro.KEY_LIST[inner_str], None, KEY_RELEASE)
                    else:
                        print 'Annotated key \'' + inner_str + '\' does not exist in my key list'
                else:
                    for i in inner_str:
                       Macro. __generate(i)

    @staticmethod
    def key_down(key):
        """
        > Description
            Hold a specific key down, useful when you want to do key combinations, like Alt + Shift to change the current keyboard layout

        > Parameters
            key (string): The key to hold down

        > Returns
            None

        > Example
            # send Alt + F4 to the current application
            key_down('Alt')
            key_down('F4')

            time.sleep(0.2)

            key_up('Alt')
            key_up('F4')
        """
        # TODO check for special keys
        if key in Macro.KEY_LIST:
            controller.generateKeyboardEvent(Macro.KEY_LIST[key], None, KEY_PRESS)

    @staticmethod
    def key_up(key):
        """
        > Description
            Hold a specific key up, useful when you want to do key combinations, like Alt + Shift to change the current keyboard layout

        > Parameters
            key (string): The key to hold up

        > Returns
            None

        > Example
            # send Alt + F4 to the current application
            key_down('Alt')
            key_down('F4')

            time.sleep(0.2)

            key_up('Alt')
            key_up('F4')
        """
        if key in Macro.KEY_LIST:
            controller.generateKeyboardEvent(Macro.KEY_LIST[key], None, KEY_RELEASE)

    def pixel_count_in_area(self, rectangle, color):
        """
        > Description
            Count the number of occurrences of a specific color on an area of the screen. You can modify which pixels to search for with the pixel search speed.

            Note that the number of occurences will be 100% accurate only with a pixel search speed of 1. See more at @ref:set_pixel_search_speed

        > Parameters
            rectangle (list): the area of the screen to search in the format [x, y, width, height]
            color (string): the HTML representation of the color to search for

        > Returns
            counter (int): the number of occurrences of the color in the searched pixels

        > Example
            m = Macro()

            # search every pixel
            m.set_pixel_search_speed(1)

            print 'There are', m.pixel_count_in_area([0, 0, 100, 100], '#000000'), 'black pixels in some part of the screen' 
        """
        x = rectangle[0]
        y = rectangle[1]
        width = rectangle[2]
        height = rectangle[3]
        color = to_lower(color)
        
        img = Macro.__grabDesktop().copy(x, y, width + 1, height + 1);
        
        counter = cur_y = cur_x = 0

        for cur_y in range(0, height + 1):
            for cur_x in range(0, width + 1, self.pixel_search_speed):
                cur_color = QColor(img.pixel(QPoint(cur_x, cur_y)))
                if(str(color) == str(cur_color.name())):
                    counter += 1

        return counter;
    
    @classmethod
    @needQApp
    def __grabDesktop(cls):
        return QPixmap.grabWindow(QApplication.desktop().winId()).toImage()

    def pixel_color_in_area(self, rectangle, color):
        """
        > Description
            Searches for a pixel with a specific color in an area of the screen.

            Note that this function is 100% accurate and will return the 1st occurrence only with a pixel search speed of 1. See more at @ref:set_pixel_search_speed

        > Parameters
            rectangle (list): the area of the screen to search in the format [x, y, width, height]
            color (string): the HTML representation of the color to search for

        > Returns
            found (bool): true if the function found a pixel with the specified color
            point (list): a list with the x, y coordinates of the found pixel. If `found` is false, then `point` will be `[-1, -1]`

        > Example
            # search for a blue pixel in an area of the screen. By default the pixel search speed is 1 so we don't need to manually set it
            found, point = Macro().pixel_color_in_area([0, 0, 1000, 500], '#0000ff')

            # if there was a pixel, click on it
            if found:
                Macro.left_click_to(point[0], point[1])
        """
        x = rectangle[0]
        y = rectangle[1]
        width = rectangle[2]
        height = rectangle[3]
        color = to_lower(color)
        
        img = Macro.__grabDesktop().copy(x, y, width + 1, height + 1);
        
        cur_y = cur_x = 0
        while( cur_y <= height ):
            cur_x = 0
            while ( cur_x <= width ):
                cur_color = QColor(img.pixel(QPoint(cur_x, cur_y)))
                if(str(color) == str(cur_color.name())):
                    return True, [cur_x+x, cur_y+y]
                cur_x += self.pixel_search_speed
            cur_y += 1

        return False, [-1, -1]
        
    @staticmethod
    def color_of_pixel(x, y):
        """
        > Description
            Returns the pixel color of the pixel at coordinates x, y
            
        > Parameters
            x (int): the x coordinate of the screen
            y (int): the y coordinate of the screen

        > Returns
           pixel_color (str): The uppercase HTML representation of the color at the x, y coordinates of the screen 

        > Example
            # get the color of the pixel 100, 100
            print Macro.color_of_pixel(100, 100)
        """
        return to_upper(str(Macro.__grabDesktop().pixel(x, y).name()))
        
    @staticmethod
    def wait_for_pixel_color(point, color, interval):
        """
        > Description
            Waits for a pixel to become a specific color
            
        > Parameters
            point (list): a list containing the x, y coordinates of the pixel on the screen
            color (str): the HTML representation of the color to wait for
            interval (int): the interval in milliseconds between each check

        > Returns
            None

        > Example
            # wait for 100, 100 to become red, checking every 1 second
            Macro.wait_for_pixel_color([100, 100], '#ff0000', 1000)

            # now the pixel has the needed color so we may continue with e.g. clicking that point
            Macro.left_click_to(100, 100)
        """
        color = to_upper(color)
        while Macro.color_of_pixel(point[0], point[1]) != color:
            time.sleep(interval / 1000.0)

    @staticmethod
    def wait_for_pixel_colors(points_colors, for_all, interval):
        """
        > Description
            Wait for pixels on the screen to match specified colors
            
        > Parameters
            points_colors (list): a list of lists. The first item of each inner list is a list containing the x, y coordinates of a pixel and the second argument is the HTML representation of the color that it should have
            for_all (bool): if true, the function will wait for all the pixels to match their colors; if false the function will wait for any of the pixels to match their colors
            interval (int): the interval in milliseconds between each check

        > Returns
            pixel_index (int): 0 if `for_all` is true. If `for_all` is false then `pixel_index` represents the index in `points_colors` that contain the pixel / color pair that satisfied the condition and made the function to quit

        > Example
            points_colors = [[[100, 100], '#ff0000'], [[200, 200], '#00ff00'], [[500, 500], '#0000ff']]

            # wait for 100, 100 to become red, 200, 200 to become green and 500, 500 to become blue, checking every 1 second
            Macro.wait_for_pixel_colors(points_colors, True, 1000)

            # wait for 100, 100 to become red or 200, 200 to become green or 500, 500 to become blue, checking every 1 second
            index = Macro.wait_for_pixel_colors(points_colors, False, 1000)

            # we can now see which pixel matched the needed color and made the function to quit
            print 'I know that the pixel', points_colors[index][0], 'is of color', points_colors[index][1]
        """

        points_count = len(points_color)

        while True:
            for index in range(points_count):
                point = points_colors[index][0]
                color = to_upper(points_colors[index][1])

                if(Macro.color_of_pixel(point[0], point[1]) == color):
                    if not for_all:
                        # found at least one that matches the needed color
                        return index
                    elif index == points_count - 1:
                        # all points checked and match
                        return 0
                elif for_all:
                    # found at least one that doesn't match the needed color
                    break

            time.sleep(interval / 1000.0)

    @staticmethod
    def wait_for_no_pixel_color(point, color, interval):
        """
        Waits till the point 'point' is not of color 'color', checking
        every 'interval' milliseconds. Then it simply exits.
        point is a tuple [x, y] while color is a string (e.g. #000000)
        """
        color = to_upper(color)
        while Macro.color_of_pixel(point[0], point[1]) == color:
            time.sleep(interval / 1000.0)

    def wait_for_pixel_color_in_area(self, rectangle, color, interval):
        """
        Waits till the rectangle 'rectangle' contains a pixel of color
        'color', checking every 'interval' milliseconds. Then it simply
        exits returning the pixel where the color was found first.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)
        """
        exists = False
        point = []
        while not exists:
            exists, point = self.pixel_color_in_area(rectangle, color)
            time.sleep(interval / 1000.0)
        return point

    def wait_for_no_pixel_color_in_area(self, rectangle, color, interval):
        """
        Waits till the rectangle 'rectangle' does not contain
        a pixel of color 'color', checking every 'interval' milliseconds.
        Then it simply exits returning the pixel where the color was found
        first.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)
        """
        exists, point = self.pixel_color_in_area(rectangle, color)
        while exists:
            time.sleep(interval / 1000.0)
            exists, point = self.pixel_color_in_area(rectangle, color)
        return point

    def wait_for_pixel_color_special(self, function, times, point, color, interval):
        """
        Waits till the point 'point' is of color 'color', checking
        every 'interval' milliseconds. It will run the function 'function'
        when it has checked 'times' times for the pixel color (and it
        hasn't found it, otherwise it exits).
        """
        if(times < 1):
            print "Invalid parameter passed for wait_for_pixel_color_special! 'times' should be 1 or more."
            return
        color = to_upper(color)
        times_counter = 0
        
        while Macro.color_of_pixel(point[0], point[1]) != color:
            times_counter += 1
            if(times==times_counter):
                times_counter = 0
                function()
            time.sleep(interval / 1000.0)

    def wait_for_no_pixel_color_special(self, function, times, point, color, interval):
        """
        Waits till the point 'point' is not of color 'color', checking
        every 'interval' milliseconds. It will run the function 'function'
        when it has checked 'times' times for the pixel color (and it
        hasn't found it, otherwise it exits).
        """
        if(times < 1):
            print "Invalid parameter passed for wait_for_pixel_color_special! 'times' should be 1 or more."
            return
        color = to_upper(color)
        times_counter = 0
        
        while Macro.color_of_pixel(point[0], point[1]) == color:
            times_counter += 1
            if(times==times_counter):
                times_counter = 0
                function()
            time.sleep(interval / 1000.0)

    def wait_for_pixel_color_in_area_special(self, function, times, rectangle, color, interval):
        """
        Waits till the rectangle 'rectangle' contains a pixel of color
        'color', checking every 'interval' milliseconds. It will run the
        function 'function' when it has checked 'times' times for the pixel
        color (and it hasn't found it, otherwise it exits).
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)
        """
        
        if(times < 1):
            print "Invalid parameter passed for wait_for_pixel_color_in_area_special! 'times' should be 1 or more."
            return
        
        times_counter = 0
        
        exists, point = self.pixel_color_in_area(rectangle, color)
        while not exists:
            times_counter += 1
            if(times_counter == times):
                times_counter = 0
                function()
            time.sleep(interval / 1000.0)
            exists, point = self.pixel_color_in_area(rectangle, color)
            
        return point

    def wait_for_no_pixel_color_in_area_special(self, function, times, rectangle, color, interval):
        """
        Waits till the rectangle 'rectangle' does not contain
        a pixel of color 'color', checking every 'interval' milliseconds.
        It will run the function 'function' when it has checked 'times'
        times for the pixel color (and it hasn't found it, otherwise it exits).
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)
        """
        
        if(times < 1):
            print "Invalid parameter passed for wait_for_pixel_color_in_area_special! 'times' should be 1 or more."
            return
        
        times_counter = 0
        
        exists, point = self.pixel_color_in_area(rectangle, color)
        while exists:
            times_counter += 1
            if(times_counter == times):
                times_counter = 0
                function()
            time.sleep(interval / 1000.0)
            exists, point = self.pixel_color_in_area(rectangle, color)
            
        return point

    @staticmethod
    def save_section_of_the_screen(rectangle, filename):
        """Saves the 'rectangle' in 'filename'.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        """
        img = Macro.__grabDesktop().copy(QRect(rectangle[0], rectangle[1], rectangle[2], rectangle[3]))
        img.save(filename, "PNG", 100);

