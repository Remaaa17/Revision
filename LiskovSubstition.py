## liskov Substition princilple ( LSP )
##==> use the polymarphism
##==> force child to use the functios that in parent by use interface
###Subtypes must be substitutable for their base types
class Animal:
    def make_sound(self):
        pass
class Dog(Animal) :
    def make_sound(self):
        print("dog sound")

class Cat(Animal) :
    def make_sound(self):
        print("cat sound")

def play_withanimal(Animal):
    Animal.make_sound()

cat=Cat()
dog=Dog()
play_withanimal(cat)
play_withanimal(dog)