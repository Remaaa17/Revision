class MyIterator:
 def _init_(self, limit):
  self.limit = limit
  self.current = 0


def _iter_(self):
  return self

def _next_(self):
  if self.current < self.limit:
   value = self.current
   self.current += 1
   return value
  else:
    raise StopIteration

iterator = MyIterator(5)
for num in iterator:
 print(num)