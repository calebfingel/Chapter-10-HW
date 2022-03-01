class Student:

    def __init__(self, studid, nam, dob, classif):
       self.__studentid = studid
       self.__name = nam
       self.__dateofbirth = dob
       self.__classification = classif


    #def set_age(self,age1)

    def set_studentid(self, studid1):
        self.__studentid = studid1
    def set_name(self,name1):
        self.__name = nam1
    def set_dateofbirth(self,dob1):
        self.__dateofbirth = dob1
    def set_classification(self,classif1):
        self.__classification = classif1

    def get_studentid(self):
        return self.__studentid
    def get_name(self):
        return self.__name
    def get_dateofbirth(self):
        return self.__dateofbirth
    def get_classification(self):
        return self.__classification