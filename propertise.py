class Circle:

 def _init_(self, radius):
  self.radius = radius # initialize the radius attribute

 @property
 def area(self): # define the area property
  return 3.14 * self.radius ** 2 # calculate the area based on the radius

 @area.setter
 def area(self, value): # define the setter for the area property
  if value < 0: # validate the input value
   raise ValueError("Area cannot be negative")
   self.radius = (value / 3.14) ** 0.5 # update the radius based on the area

C = Circle(2) # create a circle object with radius 2
print(c.area) # print the area property
# output: 12.56
c.area = 50 # set the area property to 50
print(c.radius) # print the radius attribute
# output: 3.989422804014327
c.area = -10 # set the area property to -10
# output: ValueError: Area cannot be negative

#Dataclass decorator
# 1.__init__: Initializes the object and assigns values to the attributes based on the provided arguments.
# 2.__repr__: Returns a string representation of the object.
# 3.__eq__: Compares two objects for equality based on their attribute values.
# 4.__ne__: Compares two objects for inequality based on their attribute values.
# 5.__lt__: Defines the less-than comparison between two objects.
# 6.__gt__: Defines the greater-than comparison between two objects.
# 7.__le__: Defines the less-than-or-equal-to comparison between two objects.
# 8.__ge__: Defines the greater-than-or-equal-to comparison between two objects.
person = Person("Alice", 25, "New York")
print(person)
print(person.name) # Output: Alice
person = Person("Alice", 25)
# Output: Person(name='Alice', age=25)

person = Person("Alice", 25)
print(person) # Output: Person(name='Alice', age=25)



@dataclass(repr=False)
class Point:
 x: int
 y: int

print(repr(person))
