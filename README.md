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

The above outputs some variation of:

~~~
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
~~~

# Macro

- [Static methods](#static-methods)

    - [color_of_pixel](#color_of_pixel-x-y)
    - [key_down](#key_down-key)
    - [key_up](#key_up-key)
    - [keyboard](#keyboard-key)
    - [left_click_to](#left_click_to-x-y)
    - [middle_click_to](#middle_click_to-x-y)
    - [mouse_event](#mouse_event-x-y-button-eventtype)
    - [move_cursor_to](#move_cursor_to-x-y)
    - [right_click_to](#right_click_to-x-y)
    - [save_section_of_the_screen](#save_section_of_the_screen-rectangle-filename)
    - [wait_for_no_pixel_color](#wait_for_no_pixel_color-point-color-interval)
    - [wait_for_pixel_color](#wait_for_pixel_color-point-color-interval)
    - [wait_for_pixel_colors](#wait_for_pixel_colors-points_colors-for_all-interval)

- [Instance methods](#instance-methods)

    - [pixel_color_in_area](#pixel_color_in_area-rectangle-color)
    - [pixel_count_in_area](#pixel_count_in_area-rectangle-color)
    - [set_pixel_search_speed](#set_pixel_search_speed-speed)
    - [wait_for_no_pixel_color_in_area](#wait_for_no_pixel_color_in_area-rectangle-color-interval)
    - [wait_for_no_pixel_color_in_area_special](#wait_for_no_pixel_color_in_area_special-function-times-rectangle-color-interval)
    - [wait_for_no_pixel_color_special](#wait_for_no_pixel_color_special-function-times-point-color-interval)
    - [wait_for_pixel_color_in_area](#wait_for_pixel_color_in_area-rectangle-color-interval)
    - [wait_for_pixel_color_in_area_special](#wait_for_pixel_color_in_area_special-function-times-rectangle-color-interval)
    - [wait_for_pixel_color_special](#wait_for_pixel_color_special-function-times-point-color-interval)

## Static methods

---

### `color_of_pixel (x, y)`

* **Description**

_Returns the pixel color of the pixel at coordinates x, y_

* **Parameters**

`x` (`int`): the x coordinate of the screen

`y` (`int`): the y coordinate of the screen

* **Return values**

`pixel_color` (`str`): The uppercase HTML representation of the color at the x, y coordinates of the screen

* **Example usage**

```python
# get the color of the pixel 100, 100
print Macro.color_of_pixel(100, 100)
```


---

### `key_down (key)`

* **Description**

_Hold a specific key down, useful when you want to do key combinations, like Alt + Shift to change the current keyboard layout_

* **Parameters**

`key` (`string`): The key to hold down

* **Return values**

`None`

* **Example usage**

```python
# send Alt + F4 to the current application
Macro.key_down('Alt')
Macro.key_down('F4')

time.sleep(0.2)

Macro.key_up('Alt')
Macro.key_up('F4')
```


---

### `key_up (key)`

* **Description**

_Hold a specific key up, useful when you want to do key combinations, like Alt + Shift to change the current keyboard layout_

* **Parameters**

`key` (`string`): The key to hold up

* **Return values**

`None`

* **Example usage**

```python
# send Alt + F4 to the current application
Macro.key_down('Alt')
Macro.key_down('F4')

time.sleep(0.2)

Macro.key_up('Alt')
Macro.key_up('F4')
```


---

### `keyboard (key)`

* **Description**

_Type some text or special keys, like Backspaces, Returns etc_

_For all the available keys look into `Macro.KEY_LIST`_

* **Parameters**

`key` (`string`/`list`): If the `key` is a string, then it is simpy typed out. If it is a list of strings, every string in the list will be typed out. If a string in the list starts with `@@` then it is recognized as a special key and it is not typed out as is

* **Return values**

`None`

* **Example usage**

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

### `left_click_to (x, y)`

* **Description**

_Left clicks the mouse at x, y_

* **Parameters**

`x` (`int`): the x coordinate to left click to

`y` (`int`): the y coordinate to left click to

* **Return values**

`None`

* **Example usage**

```python
# left click to 100, 100
Macro.left_click_to(100, 100)
```


---

### `middle_click_to (x, y)`

* **Description**

_Middle clicks the mouse at x, y_

* **Parameters**

`x` (`int`): the x coordinate to middle click to

`y` (`int`): the y coordinate to middle click to

* **Return values**

`None`

* **Example usage**

```python
# middle click to 100, 100
Macro.middle_click_to(100, 100)
```


---

### `mouse_event (x, y, button, eventType)`

* **Description**

_Generates a mouse press or release event on a specific pixel on the screen_

* **Parameters**

`x` (`int`): the x coordinate where the event will be generated

`y` (`int`): the y coordinate where the event will be generated

`button` (`str`): A string indicating which mouse button to press/release. One of 'left', 'right' or 'middle'

`eventType` (`str`): A string indicating the event type. One of 'press' or 'release'

* **Return values**

`None`

* **Example usage**

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

### `move_cursor_to (x, y)`

* **Description**

_Moves the cursor to the x, y coordinates_

* **Parameters**

`x` (`int`): the x coordinate to move the cursor to

`y` (`int`): the y coordinate to move the cursor to

* **Return values**

`None`

* **Example usage**

```python
# move the cursor to 100, 100
Macro.move_cursor_to(100, 100)
```


---

### `right_click_to (x, y)`

* **Description**

_Right clicks the mouse at x, y_

* **Parameters**

`x` (`int`): the x coordinate to right click to

`y` (`int`): the y coordinate to right click to

* **Return values**

`None`

* **Example usage**

```python
# right click to 100, 100
Macro.right_click_to(100, 100)
```


---

### `save_section_of_the_screen (rectangle, filename)`

* **Description**

_Saves a section of the screen as a png file, useful for OCR using other tools_

* **Parameters**

`rectangle` (`list`): the area of the screen to search in the format [x, y, width, height]

`filename` (`str`): the filename of the file to save the image

* **Return values**

`None`

* **Example usage**

```python
# save a section of the screen to /tmp/file.png
Macro.save_section_of_the_screen([100, 100, 50, 50], '/tmp/file.png')
```


---

### `wait_for_no_pixel_color (point, color, interval)`

* **Description**

_Waits for a pixel to not be of a specific color_

* **Parameters**

`point` (`list`): a list containing the x, y coordinates of the pixel on the screen

`color` (`str`): the HTML representation of the color to wait for the point to change from

`interval` (`int`): the interval in milliseconds between each check

* **Return values**

`None`

* **Example usage**

```python
# wait for pixel 100, 100 to not be red, checking every 1 second
Macro.wait_for_no_pixel_color([100, 100], '#ff0000', 1000)

# just wait for the pixel at 100, 100 to change color, checking every 1 second
Macro.wait_for_no_pixel_color([100, 100], Macro.color_of_pixel(100, 100), 1000)
```


---

### `wait_for_pixel_color (point, color, interval)`

* **Description**

_Waits for a pixel to become a specific color_

* **Parameters**

`point` (`list`): a list containing the x, y coordinates of the pixel on the screen

`color` (`str`): the HTML representation of the color to wait for

`interval` (`int`): the interval in milliseconds between each check

* **Return values**

`None`

* **Example usage**

```python
# wait for 100, 100 to become red, checking every 1 second
Macro.wait_for_pixel_color([100, 100], '#ff0000', 1000)

# now the pixel has the needed color so we may continue with e.g. clicking that point
Macro.left_click_to(100, 100)
```


---

### `wait_for_pixel_colors (points_colors, for_all, interval)`

* **Description**

_Wait for pixels on the screen to match specified colors_

* **Parameters**

`points_colors` (`list`): a list of lists. The first item of each inner list is a list containing the x, y coordinates of a pixel and the second argument is the HTML representation of the color that it should have

`for_all` (`bool`): if true, the function will wait for all the pixels to match their colors; if false the function will wait for any of the pixels to match their colors

`interval` (`int`): the interval in milliseconds between each check

* **Return values**

`pixel_index` (`int`): 0 if `for_all` is true. If `for_all` is false then `pixel_index` represents the index in `points_colors` that contain the pixel / color pair that satisfied the condition and made the function to quit

* **Example usage**

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

### `pixel_color_in_area (rectangle, color)`

* **Description**

_Searches for a pixel with a specific color in an area of the screen._

_Note that this function is 100% accurate and will return the 1st occurrence only with a pixel search speed of 1. See more at [set_pixel_search_speed](#set_pixel_search_speed-speed)_

* **Parameters**

`rectangle` (`list`): the area of the screen to search in the format [x, y, width, height]

`color` (`string`): the HTML representation of the color to search for

* **Return values**

`found` (`bool`): true if the function found a pixel with the specified color

`point` (`list`): a list with the x, y coordinates of the found pixel. If `found` is false, then `point` will be `[-1, -1]`

* **Example usage**

```python
# search for a blue pixel in an area of the screen. By default the pixel search speed is 1 so we don't need to manually set it
found, point = Macro().pixel_color_in_area([0, 0, 1000, 500], '#0000ff')

# if there was a pixel, click on it
if found:
Macro.left_click_to(point[0], point[1])
```


---

### `pixel_count_in_area (rectangle, color)`

* **Description**

_Count the number of occurrences of a specific color on an area of the screen. You can modify which pixels to search for with the pixel search speed._

_Note that the number of occurences will be 100% accurate only with a pixel search speed of 1. See more at [set_pixel_search_speed](#set_pixel_search_speed-speed)_

* **Parameters**

`rectangle` (`list`): the area of the screen to search in the format [x, y, width, height]

`color` (`string`): the HTML representation of the color to search for

* **Return values**

`counter` (`int`): the number of occurrences of the color in the searched pixels

* **Example usage**

```python
m = Macro()

# search every pixel
m.set_pixel_search_speed(1)

print 'There are', m.pixel_count_in_area([0, 0, 100, 100], '#000000'), 'black pixels in some part of the screen'
```


---

### `set_pixel_search_speed (speed)`

* **Description**

_Set the search speed (aka the number of pixels to skip forward on each iteration) for functions that search for pixel colors in areas of the screen._

_Use this method when the searched color is known to be present on continuous areas of the screen, so as to speed up the search operation._

_Use with caution when the searched color is present in areas with width smaller than the pixel search speed._

_The default value of the pixel search speed is 1_

* **Parameters**

`speed` (`int`): the number of pixels to add to the current pixel while searching. E.g. if speed is 3 then after reading pixel #1 it will skip to pixel #1+3 = #4, skipping 2 pixels

* **Return values**

`None`

* **Example usage**

```python
m = new Macro()

# set the pixel search speed to 3
m.set_pixel_search_speed(3)

# now search in the rectangle [100, 200, 500, 500] for a green pixel, skipping 2 pixels each time (searching only 1/3 of the pixels)
found, point = m.pixel_color_in_area([100, 200, 500, 500], '#00ff00')
```


---

### `wait_for_no_pixel_color_in_area (rectangle, color, interval)`

* **Description**

_Waits for a specific color to not be present in an area of the screen_

_Please note that this function is 100% accurate only with a pixel search speed of 1. See more at [set_pixel_search_speed](#set_pixel_search_speed-speed)_

* **Parameters**

`rectangle` (`list`): the area of the screen to search in the format [x, y, width, height]

`color` (`str`): the HTML representation of the color to search for

`interval` (`int`): the interval in milliseconds between each check

* **Return values**

`None`

* **Example usage**

```python
# wait till there are no black pixels in an area of the screen
Macro.wait_for_no_pixel_color_in_area([0, 0, 500, 500], '#000000', 5000)

print 'there are no black pixels at [0, 0, 500, 500]'
```


---

### `wait_for_no_pixel_color_in_area_special (function, times, rectangle, color, interval)`

* **Description**

_The same as [wait_for_pixel_color_in_area_special](#wait_for_pixel_color_in_area_special-function-times-rectangle-color-interval) but instead waits the specified area of the screen to not contain the specified color_


---

### `wait_for_no_pixel_color_special (function, times, point, color, interval)`

* **Description**

_The same as [wait_for_pixel_color_special](#wait_for_pixel_color_special-function-times-point-color-interval) but instead waits the specified pixel to not be the specified color_


---

### `wait_for_pixel_color_in_area (rectangle, color, interval)`

* **Description**

_Waits for a specific color to be found in an area of the screen_

_Please note that this function is 100% accurate only with a pixel search speed of 1. See more at [set_pixel_search_speed](#set_pixel_search_speed-speed)_

* **Parameters**

`rectangle` (`list`): the area of the screen to search in the format [x, y, width, height]

`color` (`str`): the HTML representation of the color to search for

`interval` (`int`): the interval in milliseconds between each check

* **Return values**

`point` (`list`): the point that contains the x, y coordinates of the pixel found to have the specified color

* **Example usage**

```python
# wait till the function finds a black pixel in an area of the screen, checking every 5 seconds
point = Macro.wait_for_pixel_color_in_area([0, 0, 500, 500], '#000000', 5000)

print 'black found at', point
```


---

### `wait_for_pixel_color_in_area_special (function, times, rectangle, color, interval)`

* **Description**

_The same as [wait_for_pixel_color_special](#wait_for_pixel_color_special-function-times-point-color-interval) but instead waits the specified area of the screen to contain the specified color_


---

### `wait_for_pixel_color_special (function, times, point, color, interval)`

* **Description**

_Waits for a pixel to be of specific color. In between checking this method will run a user provided function to run which can command this method to quit_

_This method will exit either because the pixel becomes the specified color or the user provided function returns false_

* **Parameters**

`function` (`function`): the function to run every `times` checks. The function can return false to make this method to quit without waiting for the pixel to become the specified color

`times` (`int`): the times to wait `interval` milliseconds before running `function`

`point` (`list`): the point containing the x, y coordinates of the pixel

`color` (`str`): the HTML representation of the color to wait for

`interval` (`int`): the interval in milliseconds between each check

* **Return values**

`None`

* **Example usage**

```python
# returns true if the mouse cursor is not at the top left corner of the screen
def mouse_not_top_left():
return Macro.get_cursor_pos() != [0, 0]

# will exit if the pixel 100, 100 becomes green (checking every 1 second)
# or if the mouse position is at 0, 0 (checking every 2 * 1 = 2 seconds)
Macro().wait_for_pixel_color_special(mouse_not_top_left, 2, [100, 100], '#00ff00', 1000)
```


This documentation was automatically formated for github by [pydoc2gitmd](#https://github.com/hytromo/pydoc2gitmd)
