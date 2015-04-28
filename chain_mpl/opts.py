class Opts(object):

  def __init__(self):
    self.opts = {}

  def merge(self, obj):
    """Merge options from different Opts objects"""
    self.opts.update(obj.opts)

  def merge_subopt(self, obj, key):
    if key in obj.opts and key in self.opts:
      self.opts[key].update(obj.opts[key])
      del obj.opts[key]

  def defaults(self, defaults, **kwargs):
    if kwargs != None: defaults.update(kwargs)
    return defaults
