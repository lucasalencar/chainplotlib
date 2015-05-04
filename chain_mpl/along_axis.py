from opts import Opts

class AlongAxis(Opts):

  def merge(self, obj):
    key = 'along_x'
    if key in obj.opts and key in self.opts:
      self.opts[key] += obj.opts[key]
      del obj.opts[key]
    super(AlongAxis, self).merge(obj)

  def along_x(self, xcoords, y = -0.1, label = '', fontsize = 12, **kwargs):
    if 'along_x' not in self.opts:
      self.opts['along_x'] = []
    arrow = dict(arrowprops = dict(arrowstyle = "|-|", connectionstyle = "arc3"))
    opt = dict(
      xcoords = xcoords,
      y = y,
      label = label,
      fontsize = fontsize,
      args = self.defaults(arrow, **kwargs)
    )
    self.opts['along_x'].append(opt)
    return self

  def plot(self, ax, x, y, **kwargs):
    if 'along_x' in self.opts:
      for an in self.opts['along_x']:
        print an
        ax.annotate("",
          xy = (an['xcoords'][0], an['y']),
          xytext = (an['xcoords'][1], an['y']),
          **an['args']
        )
        if bool(an['label']):
          label_x = (an['xcoords'][1] - an['xcoords'][0])/2.0 + an['xcoords'][0]
          label_y = an['y'] - (0.05)
          ax.text(label_x, label_y, an['label'], ha = 'center', va = 'center', fontsize = an['fontsize'])
