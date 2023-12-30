class MyClass:
 def _init_(self):
  self.public_var = "I am public"
  self. _single_underscore_var = "I am supposed to be private"
  self .__double_underscore_var = "I am also private, but with name mangling"

mc = MyClass()
print(mc.public_var) # Output: I am public
print(mc._single_underscore_var) # Output: I am supposed to be private
print(mc._MyClass__double_underscore_var) # Output: I am also private, but with name mangling