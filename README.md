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

Below you can see the result (on the left) of a python script using `macropolo` (on the right)

![MacroPolo example usage](http://i.imgur.com/aXj0Sjg.gif)

Here's another example that uses some pixel and cursor functions

![MacroPolo pixel functions](http://i.imgur.com/dH5wKeg.gif)

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

# Macro

- [Static methods](#static-methods)

    - [color_of_pixel](#color_of_pixel)
    - [key_down](#key_down)
    - [key_up](#key_up)
    - [keyboard](#keyboard)
    - [left_click_to](#left_click_to)
    - [middle_click_to](#middle_click_to)
    - [mouse_event](#mouse_event)
    - [move_cursor_to](#move_cursor_to)
    - [right_click_to](#right_click_to)
    - [save_section_of_the_screen](#save_section_of_the_screen)
    - [wait_for_no_pixel_color](#wait_for_no_pixel_color)
    - [wait_for_pixel_color](#wait_for_pixel_color)
    - [wait_for_pixel_colors](#wait_for_pixel_colors)

- [Instance methods](#instance-methods)

    - [pixel_color_in_area](#pixel_color_in_area)
    - [pixel_count_in_area](#pixel_count_in_area)
    - [set_pixel_search_speed](#set_pixel_search_speed)
    - [wait_for_no_pixel_color_in_area](#wait_for_no_pixel_color_in_area)
    - [wait_for_no_pixel_color_in_area_special](#wait_for_no_pixel_color_in_area_special)
    - [wait_for_no_pixel_color_special](#wait_for_no_pixel_color_special)
    - [wait_for_pixel_color_in_area](#wait_for_pixel_color_in_area)
    - [wait_for_pixel_color_in_area_special](#wait_for_pixel_color_in_area_special)
    - [wait_for_pixel_color_special](#wait_for_pixel_color_special)

## Static methods

---

### `color_of_pixel`

> **Description**

_Returns the pixel color of the pixel at coordinates x, y_

> **Parameters**

`x` (`int`) the x coordinate of the screen

`y` (`int`) the y coordinate of the screen

> **Return values**

`pixel_color` (`str`) The uppercase HTML representation of the color at the x, y coordinates of the screen

> **Example usage**

```python
# get the color of the pixel 100, 100
print Macro.color_of_pixel(100, 100)
```


---

### `key_down`

> **Description**

_Hold a specific key down, useful when you want to do key combinations, like Alt + Shift to change the current keyboard layout_

> **Parameters**

`key` (`string`) The key to hold down

> **Return values**

`None`

> **Example usage**

```python
# send Alt + F4 to the current application
key_down('Alt')
key_down('F4')

time.sleep(0.2)

key_up('Alt')
key_up('F4')
```


---

### `key_up`

> **Description**

_Hold a specific key up, useful when you want to do key combinations, like Alt + Shift to change the current keyboard layout_

> **Parameters**

`key` (`string`) The key to hold up

> **Return values**

`None`

> **Example usage**

```python
# send Alt + F4 to the current application
key_down('Alt')
key_down('F4')

time.sleep(0.2)

key_up('Alt')
key_up('F4')
```


---

### `keyboard`

> **Description**

_Type some text or special keys, like Backspaces, Returns etc_

_For all the available keys look into `Macro.KEY_LIST`_

> **Parameters**

`key` (`string`/`list`) If the `key` is a string, then it is simpy typed out. If it is a list of strings, every string in the list will be typed out. If a string in the list starts with `@@` then it is recognized as a special key and it is not typed out as is

> **Return values**

`None`

> **Example usage**

```python
sentence = 'alex is awesome'

# types out 'alex is awesome'
Macro.keyboard(sentence)

# types out '@@BackSpace'
Macro.keyboard('@@BackSpace')

# sends a backspace (deletes a character)
Macro.keyboard(['@@BackSpace'])

# types out 'alex is awesome' and then proceeds to go to the next line
Macro.keyboard([sentence, '@@Return'])
```


---

### `left_click_to`

> **Description**

_Left clicks the mouse at x, y_

> **Parameters**

`x` (`int`) the x coordinate to left click to

`y` (`int`) the y coordinate to left click to

> **Return values**

`None`

> **Example usage**

```python
# left click to 100, 100
Macro.left_click_to(100, 100)
```


---

### `middle_click_to`

> **Description**

_Middle clicks the mouse at x, y_

> **Parameters**

`x` (`int`) the x coordinate to middle click to

`y` (`int`) the y coordinate to middle click to

> **Return values**

`None`

> **Example usage**

```python
# middle click to 100, 100
Macro.middle_click_to(100, 100)
```


---

### `mouse_event`

> **Description**

_Generates a mouse press or release event on a specific pixel on the screen_

> **Parameters**

`x` (`int`) the x coordinate where the event will be generated

`y` (`int`) the y coordinate where the event will be generated

`button` (`str`) A string indicating which mouse button to press/release. One of 'left', 'right' or 'middle'

`eventType` (`str`) A string indicating the event type. One of 'press' or 'release'

> **Return values**

`None`

> **Example usage**

```python
# this example could demonstrate a drag and drop of a file

# press the left mouse button at 100, 100
Macro.mouse_event(100, 100, 'left', 'press')
# move the cursor to 400, 400
Macro.move_cursor_to(400, 400)
# then, release the mouse
Macro.mouse_event(400, 400, 'left', 'press')
```


---

### `move_cursor_to`

> **Description**

_Moves the cursor to the x, y coordinates_

> **Parameters**

`x` (`int`) the x coordinate to move the cursor to

`y` (`int`) the y coordinate to move the cursor to

> **Return values**

`None`

> **Example usage**

```python
# move the cursor to 100, 100
Macro.move_cursor_to(100, 100)
```


---

### `right_click_to`

> **Description**

_Right clicks the mouse at x, y_

> **Parameters**

`x` (`int`) the x coordinate to right click to

`y` (`int`) the y coordinate to right click to

> **Return values**

`None`

> **Example usage**

```python
# right click to 100, 100
Macro.right_click_to(100, 100)
```


---

### `save_section_of_the_screen`

Saves the 'rectangle' in 'filename'.The rectangle is a tuple [x, y, width, height], where x, y thecoordinates of the top left corner and width, height the widthand the height of the rectangle.

---

### `wait_for_no_pixel_color`

Waits till the point 'point' is not of color 'color', checkingevery 'interval' milliseconds. Then it simply exits.point is a tuple [x, y] while color is a string (e.g. #000000)

---

### `wait_for_pixel_color`

> **Description**

_Waits for a pixel to become a specific color_

> **Parameters**

`point` (`list`) a list containing the x, y coordinates of the pixel on the screen

`color` (`str`) the HTML representation of the color to wait for

`interval` (`int`) the interval in milliseconds between each check

> **Return values**

`None`

> **Example usage**

```python
# wait for 100, 100 to become red, checking every 1 second
Macro.wait_for_pixel_color([100, 100], '#ff0000', 1000)

# now the pixel has the needed color so we may continue with e.g. clicking that point
Macro.left_click_to(100, 100)
```


---

### `wait_for_pixel_colors`

> **Description**

_Wait for pixels on the screen to match specified colors_

> **Parameters**

`points_colors` (`list`) a list of lists. The first item of each inner list is a list containing the x, y coordinates of a pixel and the second argument is the HTML representation of the color that it should have

`for_all` (`bool`) if true, the function will wait for all the pixels to match their colors; if false the function will wait for any of the pixels to match their colors

`interval` (`int`) the interval in milliseconds between each check

> **Return values**

`pixel_index` (`int`) 0 if `for_all` is true. If `for_all` is false then `pixel_index` represents the index in `points_colors` that contain the pixel / color pair that satisfied the condition and made the function to quit

> **Example usage**

```python
points_colors = [[[100, 100], '#ff0000'], [[200, 200], '#00ff00'], [[500, 500], '#0000ff']]

# wait for 100, 100 to become red, 200, 200 to become green and 500, 500 to become blue, checking every 1 second
Macro.wait_for_pixel_colors(points_colors, True, 1000)

# wait for 100, 100 to become red or 200, 200 to become green or 500, 500 to become blue, checking every 1 second
index = Macro.wait_for_pixel_colors(points_colors, False, 1000)

# we can now see which pixel matched the needed color and made the function to quit
print 'I know that the pixel', points_colors[index][0], 'is of color', points_colors[index][1]
```


## Instance methods

---

### `pixel_color_in_area`

> **Description**

_Searches for a pixel with a specific color in an area of the screen._

_Note that this function is 100% accurate and will return the 1st occurrence only with a pixel search speed of 1. See more at [set_pixel_search_speed](#set_pixel_search_speed)_

> **Parameters**

`rectangle` (`list`) the area of the screen to search in the format [x, y, width, height]

`color` (`string`) the HTML representation of the color to search for

> **Return values**

`found` (`bool`) true if the function found a pixel with the specified color

`point` (`list`) a list with the x, y coordinates of the found pixel. If `found` is false, then `point` will be `[-1, -1]`

> **Example usage**

```python
# search for a blue pixel in an area of the screen. By default the pixel search speed is 1 so we don't need to manually set it
found, point = Macro().pixel_color_in_area([0, 0, 1000, 500], '#0000ff')

# if there was a pixel, click on it
if found:
Macro.left_click_to(point[0], point[1])
```


---

### `pixel_count_in_area`

> **Description**

_Count the number of occurrences of a specific color on an area of the screen. You can modify which pixels to search for with the pixel search speed._

_Note that the number of occurences will be 100% accurate only with a pixel search speed of 1. See more at [set_pixel_search_speed](#set_pixel_search_speed)_

> **Parameters**

`rectangle` (`list`) the area of the screen to search in the format [x, y, width, height]

`color` (`string`) the HTML representation of the color to search for

> **Return values**

`counter` (`int`) the number of occurrences of the color in the searched pixels

> **Example usage**

```python
m = Macro()

# search every pixel
m.set_pixel_search_speed(1)

print 'There are', m.pixel_count_in_area([0, 0, 100, 100], '#000000'), 'black pixels in some part of the screen'
```


---

### `set_pixel_search_speed`

> **Description**

_Set the search speed (aka the number of pixels to skip forward on each iteration) for functions that search for pixel colors in areas of the screen._

_Use this method when the searched color is known to be present on continuous areas of the screen, so as to speed up the search operation._

_Use with caution when the searched color is present in areas with width smaller than the pixel search speed._

_The default value of the pixel search speed is 1_

> **Parameters**

`speed` (`int`) the number of pixels to add to the current pixel while searching. E.g. if speed is 3 then after reading pixel #1 it will skip to pixel #1+3 = #4, skipping 2 pixels

> **Return values**

`None`

> **Example usage**

```python
m = new Macro()

# set the pixel search speed to 3
m.set_pixel_search_speed(3)

# now search in the rectangle [100, 200, 500, 500] for a green pixel, skipping 2 pixels each time (searching only 1/3 of the pixels)
found, point = m.pixel_color_in_area([100, 200, 500, 500], '#00ff00')
```


---

### `wait_for_no_pixel_color_in_area`

Waits till the rectangle 'rectangle' does not containa pixel of color 'color', checking every 'interval' milliseconds.Then it simply exits returning the pixel where the color was foundfirst.The rectangle is a tuple [x, y, width, height], where x, y thecoordinates of the top left corner and width, height the widthand the height of the rectangle.The color is a string with a hexadecimal representation ofa color (e.g. #000000)

---

### `wait_for_no_pixel_color_in_area_special`

Waits till the rectangle 'rectangle' does not containa pixel of color 'color', checking every 'interval' milliseconds.It will run the function 'function' when it has checked 'times'times for the pixel color (and it hasn't found it, otherwise it exits).The rectangle is a tuple [x, y, width, height], where x, y thecoordinates of the top left corner and width, height the widthand the height of the rectangle.The color is a string with a hexadecimal representation ofa color (e.g. #000000)

---

### `wait_for_no_pixel_color_special`

Waits till the point 'point' is not of color 'color', checkingevery 'interval' milliseconds. It will run the function 'function'when it has checked 'times' times for the pixel color (and ithasn't found it, otherwise it exits).

---

### `wait_for_pixel_color_in_area`

Waits till the rectangle 'rectangle' contains a pixel of color'color', checking every 'interval' milliseconds. Then it simplyexits returning the pixel where the color was found first.The rectangle is a tuple [x, y, width, height], where x, y thecoordinates of the top left corner and width, height the widthand the height of the rectangle.The color is a string with a hexadecimal representation ofa color (e.g. #000000)

---

### `wait_for_pixel_color_in_area_special`

Waits till the rectangle 'rectangle' contains a pixel of color'color', checking every 'interval' milliseconds. It will run thefunction 'function' when it has checked 'times' times for the pixelcolor (and it hasn't found it, otherwise it exits).The rectangle is a tuple [x, y, width, height], where x, y thecoordinates of the top left corner and width, height the widthand the height of the rectangle.The color is a string with a hexadecimal representation ofa color (e.g. #000000)

---

### `wait_for_pixel_color_special`

Waits till the point 'point' is of color 'color', checkingevery 'interval' milliseconds. It will run the function 'function'when it has checked 'times' times for the pixel color (and ithasn't found it, otherwise it exits).


