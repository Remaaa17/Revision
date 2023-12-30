### single responsibility principle ( SRP )
##==> class have one task

class FileManger:
    def read(self,file_path):
        pass
    def write(self,file_path):
        pass

class DataProcessor:
    def processdata(self,data):
        pass

class DataAnalyzes:
    def analayzedata(self,data):
        pass


class ReportGenerator:
    def generatereport(self, data):
        pass

