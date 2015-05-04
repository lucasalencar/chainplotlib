import matplotlib.pyplot as plt

from axis import Axis
from marks import Marks
from along_axis import AlongAxis

class Plot(object):

  def __init__(self, figsize = (14,8), options = {}, **kwargs):
    self.fig = plt.figure(figsize = figsize, **kwargs)
    self.plots = []
    self.options = options

  def printit(self, fname = ''):
    plt.show() if fname == '' else plt.savefig(fname)
    return self

  def add_opts(self, key, opts):
    if key in self.options:
      self.options[key].merge(opts)
    else:
      self.options[key] = opts
    return self

  def add(self, x, y, title = ''):
    self.plots.append(dict(x = x, y = y, title = title))
    return self

  def plot(self, rows = 1, cols = 1, **kwargs):
    if rows * cols >= len(self.plots):
      for i in range(len(self.plots)):
        ax = self.fig.add_subplot(rows, cols, i + 1)
        self.subplot(ax, i, **kwargs)
    else:
      raise Exception("The combination (%s, %s) is not enough for %s plots." % (rows, cols, len(self.plots)))
    return self

  def subplot(self, ax, i, **kwargs):
    x = self.plots[i]['x']; y = self.plots[i]['y']
    ax.plot(x, y, **kwargs)
    self.plot_options(ax, x, y, i)

  def plot_options(self, ax, x, y, i):
    if bool(self.plots[i]['title']):
      ax.set_title(self.plots[i]['title'])
    if 'axis_zero' in self.options:
      self.options['axis_zero'].plot(ax, x, y)
    if 'marks' in self.options:
      self.options['marks'].plot(ax, x, y)
    if 'marks_%s' % i in self.options:
      self.options['marks_%s' % i].plot(ax, x, y)
    if 'axis' in self.options:
      self.options['axis'].plot(ax, x, y)
    if 'along_axis' in self.options:
      self.options['along_axis'].plot(ax, x, y)

  def ax_labels(self, xlabel = '', ylabel = '', **kwargs):
    """Sets the axis X and Y labels"""
    self.add_opts('axis', Axis().labels(xlabel, ylabel, **kwargs))
    return self

  def limits(self, xmin = None, xmax = None, ymin = None, ymax = None):
    """Sets up the limits that the plot is showed."""
    self.add_opts('axis', Axis().limits(xmin, xmax, ymin, ymax))
    return self

  def fill(self, **kwargs):
    """Sets up to all the plots be filled."""
    self.add_opts('marks', Marks().fill(**kwargs))
    return self

  def axis_zero(self, **kwargs):
    """Activates line that marks the axis X at Y = 0"""
    self.add_opts('axis_zero', Marks().hline(0, **kwargs))
    return self

  def mark_x(self, x, i = 0, **kwargs):
    if i == 0: i = len(self.plots) - 1
    self.add_opts('marks_%s' % i, Marks().mark_x(x, **kwargs))
    return self

  def mark_y(self, y, i = 0, **kwargs):
    if i == 0: i = len(self.plots) - 1
    self.add_opts('marks_%s' % i, Marks().mark_y(y, **kwargs))
    return self

  def xticks(self, inc = None, size = None):
    self.add_opts('axis', Axis().xticks(inc = inc, size = size))
    return self

  def yticks(self, inc = None, size = None):
    self.add_opts('axis', Axis().yticks(inc = inc, size = size))
    return self

  def ticks(self, inc = None, size = None):
    self.add_opts('axis', Axis().ticks(inc = inc, size = size))
    return self

  def along_x(self, xcoords, y = -0.1, label = '', fontsize = 12, **kwargs):
    self.add_opts('along_axis', AlongAxis().along_x(xcoords, y, label, fontsize, **kwargs))
    return self
