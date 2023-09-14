# from tech import *
class coures:
    def __init__(self,code,name,year,numOFsection,teacherANDsec):
        self.code = code
        self.name = name
        self.year = year
        self.numOFsection = numOFsection
        self.teacherANDsec = teacherANDsec

    def tostring(self):
        return self.code + " " + self.name
    def printTe(self):
        for x in self.teacherANDsec:
            print(x.tostr())