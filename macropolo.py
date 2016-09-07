#!/usr/bin/env python
import gi
gi.require_version('Atspi', '2.0')

from gi.repository import Atspi
from pyatspi import Registry as controller
from pyatspi import (KEY_SYM, KEY_PRESS, KEY_PRESSRELEASE, KEY_RELEASE, MOUSE_ABS)
from PyQt4.QtGui import QPixmap, QApplication, QColor, QImage, QDesktopWidget, QCursor
from PyQt4.QtCore import QPoint, QRect
import sys, time

key_list = {
        "1":10, "2":11, "3":12, "4":13, "5":14, "6":15, "7":16, "8":17, "9":18, "0":19, "-":20, "=":21, "`":49, ".":60, "Esc":9, "Shift":50, "Win":133, "Up":111, "Down":116, "Left":113, "Right":114, "Ctrl":37, "Alt":64, "space":65, " ":65, "Return":36, "A":38, "B":56, "C":54, "D":40, "E":26, "F":41, "G":42, "H":43, "I":31, "J":44, "K":45, "L":46, "M":58, "N":57, "O":32, "P":33, "Q":24, "R":27, "S":39, "T":28, "U":30, "V":55, "W":25, "X":53, "Y":29, "Z":52, "a":38, "b":56, "c":54, "d":40, "e":26, "f":41, "g":42, "h":43, "i":31, "j":44, "k":45, "l":46, "m":58, "n":57, "o":32, "p":33, "q":24, "r":27, "s":39, "t":28, "u":30, "v":55, "w":25, "x":53, "y":29, "z":52, "F1":67, "F2":68, "F3":69, "F4":70, "F5":71, "F6":72, "F7":73, "F8":74, "F9":75, "F10":76, "F11":95, "F12":96, "BackSpace":22
}

shift_key_list = {
    "!": key_list["1"],
    "@": key_list["2"],
    "#": key_list["3"],
    "$": key_list["4"],
    "%": key_list["5"],
    "^": key_list["6"],
    "&": key_list["7"],
    "*": key_list["8"],
    "(": key_list["9"],
    ")": key_list["0"],
    "_": key_list["-"],
    "+": key_list["="]
}

app = QApplication(sys.argv)

def to_upper(string):
    """Returns python or Qt String to upper"""
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


class Macro:
    def __init__(self):
        self.pixel_search_speed=1;

    def setPixelSearchSpeed(self, speed):
        self.pixel_search_speed=speed;

    @staticmethod
    def move_cursor_to(x, y):
        """Moves the cursor to the x, y coordinates"""
        controller.generateMouseEvent(x, y, MOUSE_ABS)
    
    @staticmethod
    def get_cursos_pos():
        """Returns the cursor pos as a tuple"""
        return [QCursor.pos().x(), QCursor.pos().y()]

    @staticmethod
    def left_click_to(x, y):
        """Left clicks the cursor to the x, y coordinates"""
        if(x >= 0 and y >= 0):
            controller.generateMouseEvent(x, y, 'b1c')
            
    @staticmethod
    def middle_click_to(x, y):
        """Middle clicks the cursor to the x, y coordinates"""
        if(x >= 0 and y >= 0):
            controller.generateMouseEvent(x, y, 'b2c')
            
    @staticmethod
    def right_click_to(x, y):
        """Right clicks the cursor to the x, y coordinates"""
        if(x >= 0 and y >= 0):
            controller.generateMouseEvent(x, y, 'b3c')
    
    @staticmethod
    def __generate(i):
        inShiftKeyList = i in shift_key_list
        if not (i in key_list or inShiftKeyList):
            print 'Cannot type the character \'' + i +'\''

        needShift = inShiftKeyList or i.isupper()

        if needShift:
            controller.generateKeyboardEvent(key_list['Shift'], None, KEY_PRESS)

        controller.generateKeyboardEvent((shift_key_list if inShiftKeyList else key_list)[i], None, KEY_PRESS)
        time.sleep(0.01)
        controller.generateKeyboardEvent((shift_key_list if inShiftKeyList else key_list)[i], None, KEY_RELEASE)

        if needShift:
            controller.generateKeyboardEvent(key_list['Shift'], None, KEY_RELEASE)

    @staticmethod
    def keyboard(key):
        """
        Types the tuple 'key' to the screen. For example you can say:
        ["Alex was in a bad mood lately", "Return", "A", "B", "1", "2", "comma"] and it will try to print:
        Alex was in a bad mood lately
        AB12,
        A simple string rather than a tuple may as well be passed to this function.
        """
        if type(key) is str:
            for i in key:
               Macro. __generate(i)
        elif type(key) in [tuple, list]:
            for inner_str in key:
                if inner_str.startswith('@@'):
                    inner_str = inner_str[2:]
                    if inner_str in key_list:
                        controller.generateKeyboardEvent(key_list[inner_str], None, KEY_PRESS)
                        time.sleep(0.01)
                        controller.generateKeyboardEvent(key_list[inner_str], None, KEY_RELEASE)
                    else:
                        print 'Annotated key \'' + inner_str + '\' does not exist in my key list'
                else:
                    for i in inner_str:
                       Macro. __generate(i)

    @staticmethod
    def key_down(key):
        """
        This is a more specific function than keyboard(). It can send specific
        key-pressed events, in case you want to do keyboard combinations, like Alt+F4
        The argument can only be a string. If you want to send (e.g.) Alt+F4 then you
        should call it as:
        key_down("Alt")
        key_down("F4")
        time.sleep(0.2)
        key_up("Alt")
        key_up("F4")
        """
        if key in key_list:
            controller.generateKeyboardEvent(key_list[key], None, KEY_PRESS)

    @staticmethod
    def key_up(key):
        """
        It releases a pressed key. See the key_down(key) function for more info.
        """
        if key in key_list:
            controller.generateKeyboardEvent(key_list[key], None, KEY_RELEASE)

    def pixel_color_in_area_counter(self, rectangle, color):
        """
        Searches the rectangle area 'rectangle' for the color 'color'.
        It returns an integer indicating the times that the 'color'
        was found inside the 'rectangle'.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)
        """
        x = rectangle[0]
        y = rectangle[1]
        width = rectangle[2]
        height = rectangle[3]
        color = to_lower(color)
        
        img = QPixmap.grabWindow(QApplication.desktop().winId()).toImage().copy(x, y, width+1, height+1);
        
        counter=cur_y=cur_x=0
        while( cur_y <= height ):
            cur_x=0
            while ( cur_x <= width ):
                cur_color = QColor(img.pixel(QPoint(cur_x, cur_y)))
                if(str(color)==str(cur_color.name())):
                    counter+=1
                cur_x+=self.pixel_search_speed
            cur_y+=1
        return counter;

    def pixel_color_in_area(self, rectangle, color):
        """
        Searches the rectangle area 'rectangle' for the color 'color'.
        If the 'color' is found inside 'rectangle' then it returns True
        as first argument and the point where the pixel was found as the 2nd argument
        If nothing is found then it simply returns False.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)
        """
        x = rectangle[0]
        y = rectangle[1]
        width = rectangle[2]
        height = rectangle[3]
        color = to_lower(color)
        
        img = QPixmap.grabWindow(QApplication.desktop().winId()).toImage().copy(x, y, width+1, height+1);
        
        cur_y=cur_x=0
        while( cur_y <= height ):
            cur_x=0
            while ( cur_x <= width ):
                cur_color = QColor(img.pixel(QPoint(cur_x, cur_y)))
                if(str(color)==str(cur_color.name())):
                    return True, [cur_x+x, cur_y+y]
                cur_x+=self.pixel_search_speed
            cur_y+=1
        return False, [-1, -1]
        
    @staticmethod
    def color_of_pixel(x, y):
        """Returns the pixel color of the pixel at coordinates x, y."""
        c = QColor(QPixmap.grabWindow(QApplication.desktop().winId()).toImage().pixel(x, y))
        return to_upper(str(c.name()))
        
    @staticmethod
    def wait_for_pixel_color(point, color, timeout):
        """
        Waits till the point 'point' is of color 'color', checking
        every 'timeout' milliseconds. Then it simply exits.
        point is a tuple [x, y]
        """
        color=to_upper(color)
        while color_of_pixel(point[0], point[1]) != color:
            time.sleep(timeout / 1000.0)

    @staticmethod
    def wait_for_pixel_colors(points_colors, for_all, timeout):
        """
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
        """
        if not for_all:
            found = False
            index=0
            while not found:
                index=0
                for pair in points_colors:
                    point = pair[0]
                    color = pair[1]
                    if(color_of_pixel(point[0], point[1]) == color):
                        found = True
                        break
                    index+=1
                time.sleep(timeout/1000.0)
            return index
        else:
            while True:
                cur_checked = 0
                for pair in points_colors:
                    point = pair[0]
                    color = pair[1]
                    if(color_of_pixel(point[0], point[1]) == color):
                        cur_checked+=1
                        if(cur_checked==len(points_color)):
                            return 0
                    else:
                        break;
                time.sleep(timeout/1000.0)
            
    @staticmethod
    def wait_for_no_pixel_color(point, color, timeout):
        """
        Waits till the point 'point' is not of color 'color', checking
        every 'timeout' milliseconds. Then it simply exits.
        point is a tuple [x, y] while color is a string (e.g. #000000)
        """
        color=to_upper(color)
        while self.color_of_pixel(point[0], point[1]) == color:
            time.sleep(timeout/1000.0)

    def wait_for_pixel_color_in_area(self, rectangle, color, timeout):
        """
        Waits till the rectangle 'rectangle' contains a pixel of color
        'color', checking every 'timeout' milliseconds. Then it simply
        exits returning the pixel where the color was found first.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        The color is a string with a hexadecimal representation of 
        a color (e.g. #000000)
        """
        exists, point = self.pixel_color_in_area(rectangle, color)
        while not exists:
            time.sleep(timeout/1000.0)
            exists, point = self.pixel_color_in_area(rectangle, color)
        return point

    def wait_for_no_pixel_color_in_area(self, rectangle, color, timeout):
        """
        Waits till the rectangle 'rectangle' does not contain
        a pixel of color 'color', checking every 'timeout' milliseconds.
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
            time.sleep(timeout / 1000.0)
            exists, point = self.pixel_color_in_area(rectangle, color)
        return point

    def wait_for_pixel_color_special(self, function, times, point, color, timeout):
        """
        Waits till the point 'point' is of color 'color', checking
        every 'timeout' milliseconds. It will run the function 'function'
        when it has checked 'times' times for the pixel color (and it
        hasn't found it, otherwise it exits).
        """
        if(times < 1):
            print "Invalid parameter passed for wait_for_pixel_color_special! 'times' should be 1 or more."
            return
        color=to_upper(color)
        times_counter=0
        
        while self.color_of_pixel(point[0], point[1]) != color:
            times_counter+=1
            if(times==times_counter):
                times_counter=0
                function()
            time.sleep(timeout/1000.0)

    def wait_for_no_pixel_color_special(self, function, times, point, color, timeout):
        """
        Waits till the point 'point' is not of color 'color', checking
        every 'timeout' milliseconds. It will run the function 'function'
        when it has checked 'times' times for the pixel color (and it
        hasn't found it, otherwise it exits).
        """
        if(times < 1):
            print "Invalid parameter passed for wait_for_pixel_color_special! 'times' should be 1 or more."
            return
        color=to_upper(color)
        times_counter=0
        
        while self.color_of_pixel(point[0], point[1]) == color:
            times_counter+=1
            if(times==times_counter):
                times_counter=0
                function()
            time.sleep(timeout/1000.0)

    def wait_for_pixel_color_in_area_special(self, function, times, rectangle, color, timeout):
        """
        Waits till the rectangle 'rectangle' contains a pixel of color
        'color', checking every 'timeout' milliseconds. It will run the
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
            times_counter+=1
            if(times_counter == times):
                times_counter = 0
                function()
            time.sleep(timeout / 1000.0)
            exists, point = self.pixel_color_in_area(rectangle, color)
            
        return point

    def wait_for_no_pixel_color_in_area_special(self, function, times, rectangle, color, timeout):
        """
        Waits till the rectangle 'rectangle' does not contain
        a pixel of color 'color', checking every 'timeout' milliseconds.
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
            time.sleep(timeout / 1000.0)
            exists, point = self.pixel_color_in_area(rectangle, color)
            
        return point

    @staticmethod
    def save_section_of_the_screen(rectangle, filename):
        """Saves the 'rectangle' in 'filename'.
        The rectangle is a tuple [x, y, width, height], where x, y the
        coordinates of the top left corner and width, height the width
        and the height of the rectangle.
        """
        img = QPixmap.grabWindow(QApplication.desktop().winId()).toImage().copy(QRect(rectangle[0], rectangle[1], rectangle[2], rectangle[3]))
        img.save(filename, "PNG", 100);

