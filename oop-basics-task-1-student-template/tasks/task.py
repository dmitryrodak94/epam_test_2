class Field:
    def __init__(self, value=None):
        self.__value = value
    
    def get_value(self):
        return self.__value
    

    def set_value(self, new_value):
        self.__value = new_value
        

field = Field(20)
print(field.get_value())

field.set_value(30)
print(field.get_value())


