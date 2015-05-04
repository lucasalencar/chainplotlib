# Chainplotlib

Simple wrapper for Matplotlib that supports the design pattern of method chain.

## Installing

Clone the repository to your machine and run the setup.py script in the project.

```
$ git clone https://github.com/lucasandre/chainplotlib.git
$ cd chainplotlib
$ python setup.py install
```

This way, the lib will be available for any python script using the import:

```python
from chainplotlib import *
```

## Usage

An example of subplots with marks in the x axis, setting up the axis labels and filling the areas.

```python
from chainplotlib import *

x = [0,1,2,3,4]; y = [-1,1,-1,1,-1]
# To print in the screen
plot = Plot().add(x, y).add(x, y).plot(2, 1).printit()
# or to print in a separate file
plot = Plot().add(x, y).add(x, y).plot(2, 1).printit('plot.png')
```

Any configuration must be called before the plot() method:

The object Plot supports the following configs:

```python
ax_labels(xlabel = '', ylabel = '', **args) # The X and Y axis labels
limits(xmin = None, xmax = None, ymin = None, ymax = None) # Sets up the limits that the plot is showed
fill(**args) # Fill between the lines
axis_zero(**args) # Adds a line in the Y = 0 position
mark_x(x, i = 0, **args) # Marks a value with a line from the X axis
mark_y(y, i = 0, **args) # Marks a value with a line from the Y axis
xticks(inc = None, size = None) # Defines the increment and font size of the ticks in the X axis
yticks(inc = None, size = None) # Defines the increment and font size of the ticks in the Y axis
ticks(inc = None, size = None) # Defines the increment and font size of the ticks in both axis
along_x(xcoords, y = -0.1, label = '', fontsize = 12, **args) # Adds intervals along the X axis
mark_line_y(y, **kwargs): Adds a line in the Y position specified
mark_line_x(x, **kwargs): Adds a line in the X position specified
```

Lucas André de Alencar (c)
