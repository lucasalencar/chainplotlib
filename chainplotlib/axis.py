from opts import Opts
import numpy as np

class Axis(Opts):

  def merge(self, obj):
    self.merge_subopt(obj, 'xticks')
    self.merge_subopt(obj, 'yticks')
    super(Axis, self).merge(obj)

  def labels(self, xlabel = '', ylabel = '', **kwargs):
    """Set labels for X and Y axis"""
    if xlabel != '': self.opts['xlabel'] = xlabel
    if ylabel != '': self.opts['ylabel'] = ylabel
    if xlabel != '' or ylabel != '':
      self.opts['labels'] = kwargs
    return self

  def limits(self, xmin = None, xmax = None, ymin = None, ymax = None):
    """Sets up the limits that the plot is showed."""
    limits = {}
    if xmin != None: limits['xmin'] = xmin
    if xmax != None: limits['xmax'] = xmax
    if ymin != None: limits['ymin'] = ymin
    if ymax != None: limits['ymax'] = ymax
    if bool(limits): self.opts['limits'] = limits
    return self

  def xticks(self, inc = None, size = None):
    """Set the x ticks increment"""
    ticks = {}
    if inc != None: ticks['inc'] = inc
    if size != None: ticks['size'] = size
    if bool(ticks):
      if 'xticks' not in self.opts: self.opts['xticks'] = {}
      self.opts['xticks'].update(ticks)
    return self

  def yticks(self, inc = None, size = None):
    """Set the y ticks increment"""
    ticks = {}
    if inc != None: ticks['inc'] = inc
    if size != None: ticks['size'] = size
    if bool(ticks):
      if 'yticks' not in self.opts: self.opts['yticks'] = {}
      self.opts['yticks'].update(ticks)
    return self

  def ticks(self, inc = None, size = None):
    self.xticks(inc, size)
    self.yticks(inc, size)
    return self

  def plot(self, ax, x, y):
    if 'xlabel' in self.opts:
      ax.set_xlabel(self.opts['xlabel'], **self.opts['labels'])
    if 'ylabel' in self.opts:
      ax.set_ylabel(self.opts['ylabel'], **self.opts['labels'])
    if 'limits' in self.opts:
      ax.axis(**self.opts['limits'])
    if 'xticks' in self.opts:
      if 'inc' in self.opts['xticks']:
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.arange(start, end + 1, self.opts['xticks']['inc']))
      if 'size' in self.opts['xticks']:
        ax.tick_params(axis = 'x', labelsize = self.opts['xticks']['size'])
    if 'yticks' in self.opts:
      if 'inc' in self.opts['yticks']:
        start, end = ax.get_ylim()
        ax.yaxis.set_ticks(np.arange(start, end + 0.1, self.opts['yticks']['inc']))
      if 'size' in self.opts['yticks']:
        ax.tick_params(axis = 'y', labelsize = self.opts['yticks']['size'])
