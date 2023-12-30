from collections.abc import Sequence

class Items(Sequence):
 def _init_(self, *values):
  self ._values = list(values)

 def _len_(self):
  return len(self ._values)

def getitem (self, item):
  return self. values. getitem_(item)