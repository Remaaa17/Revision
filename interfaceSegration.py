## interface segration princciple (ISP)
##use multiple inhertance to use it  ==> to avoid force child to use all iterface
from  abc import ABC,abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self,document):
        pass
class Scanner(ABC):
    @abstractmethod
    def scan(self,document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self,document):
        pass
class old_printer(Printer):
    @abstractmethod
    def print(self,document):
        print(f"Printing {document} in black and white")

class new_printer(Printer,Fax,Scanner) :
    def print(self,document):
        print(f"Printing {document} in color")

    def scan(self,document):
        print(f"scanning {document} ...")

    def fax(self,document):
        print(f"faxing {document} ..")
