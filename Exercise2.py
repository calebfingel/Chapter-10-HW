
class phone:

    def __init__(self, man, mod, ret):
       self.__manufact = man
       self.__model = mod
       self.__retail_price = ret

    def set_manufact(self, manufact1):
        self.__manufact = manufact1
    def set_model(self,model1):
        self.__model = model1
    def set_retail_price(self,price1):
        self.__retail_price = price1

    def get_manufact(self):
        return self.__manufact
    def get_model(self):
        return self.__model
    def get_retail_price(self):
        return self.__retail_price