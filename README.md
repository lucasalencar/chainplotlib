# Chainplotlib

Simple wrapper for Matplotlib that supports the design pattern of method chain.

## Usage

An example of subplots with marks in the x axis, setting up the axis labels and filling the areas.

```python
from chainplotlib import *

x = [0,1,2,3,4]; y = [-1,1,-1,1,-1]
plot = Plot().add(x, y).mark_x(1).add(x, y).mark_x(3)
plot.ax_labels(xlabel = 'XAxis', ylabel = 'YAxis', fontsize = 15)
plot.fill(color = 'red').plot(2, 1).printit()
```

Lucas André de Alencar (c)
