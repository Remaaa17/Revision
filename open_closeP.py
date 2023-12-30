### open closed principle ( OCP )
##==> open : for extention ( can add any mehod without conflict and don't edit any funcution  ) <br>
##==> close : for  modify ( edit the code that coding before)
from  abc import ABC,abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self,shape_type):
        self.shape_type=shape_type
    @abstractmethod
    def cal_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,length):
        super().__init__("rectangle")
        self.width=width
        self.length=length

    def cal_area(self):
        return self.width * self.length
class Circle(Shape):
    def __init__(self,radius):
        super().__init__("circle")
        self.radius=radius

    def cal_area(self):
         return pi*self.radius**2

class Square(Shape):
    def __init__(self,side):
        super().__init__("square")
        self.side=side

    def cal_area(self):
        return self.side**2