MacroPolo is a python module that can be used in order to automate processes.

While it supports simple mouse movement and key strokes simulation, what really makes MacroPolo different
from other macro operations libraries or programs is that it can powerfully search your screen for pixels.

This means that you can automate many tasks depending on the current color of pixels on your screen. Using
this technic, automating complex processes (like betting at a roulette game, which is not encouraged) becomes
very easy.

# Example usage

~~~ python
from macropolo import Macro

Macro.move_cursor_to(1, 1)
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
