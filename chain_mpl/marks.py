from opts import Opts

class Marks(Opts):

  def merge(self, obj):
    self.merge_subopt(obj, 'mark_x')
    self.merge_subopt(obj, 'mark_y')
    super(Marks, self).merge(obj)

  def fill(self, **kwargs):
    """Sets up to all the plots be filled."""
    self.opts['fill_under'] = kwargs
    return self

  def mark_x(self, x, **kwargs):
    if type(x) is int: x = [x]
    self.opts['mark_x'] = { 'x': x, 'args': self.defaults({'linestyle': '--'}, **kwargs) }
    return self

  def mark_y(self, y, **kwargs):
    if type(y) is int: y = [y]
    self.opts['mark_y'] = { 'y': y, 'args': self.defaults({'linestyle': '--'}, **kwargs) }
    return self

  def hline(self, y, **kwargs):
    if type(y) is int: y = [y]
    self.opts['hline'] = {'y': y, 'args': self.defaults({'color': 'black'}, **kwargs)}
    return self

  def vline(self, x, **kwargs):
    if type(x) is int: x = [x]
    self.opts['vline'] = {'x': x, 'args': kwargs}
    return self

  def plot(self, ax, x, y, **kwargs):
    if 'fill_under' in self.opts:
      ax.fill_between(x, y, **self.opts['fill_under'])
    if 'hline' in self.opts:
      for v in self.opts['hline']['y']:
        ax.axhline(v, **self.opts['hline']['args'])
    if 'vline' in self.opts:
      for v in self.opts['vline']['y']:
        ax.axvline(v, **self.opts['vline']['args'])
    if 'mark_x' in self.opts:
      for v in self.opts['mark_x']['x']:
        idx = x.index(v)
        ax.plot([v, v], [0, y[idx]], **self.opts['mark_x']['args'])
    if 'mark_y' in self.opts:
      for v in self.opts['mark_y']['y']:
        idx = y.index(v)
        ax.plot([0, x[idx]], [v, v], **self.opts['mark_y']['args'])
