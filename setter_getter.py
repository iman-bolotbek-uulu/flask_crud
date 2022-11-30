class Student:
    def __init__(self,name):
        self.__name = name
        self.age = 18

    # def get_name(self):
    #     return self.__name

    @property
    def name(self):
        return self.__name

    # def set_name(self,new_name):
    #     if new_name.isalpha():
    #         self.__name = new_name
    #     else:
    #         raise Exception('В имени не должно быть цифр')

    @name.setter
    def name(self,new_name):
        if new_name.isalpha():
            self.__name = new_name
        else:
            raise Exception('В имени не должно быть цифр')

    @name.deleter
    def name(self):
        raise Exception('Удалять нельзя')

    # name = property(get_name,set_name,delete_name)


s = Student(name='Iman')
# print(s.get_name())
# s.set_name("Myrza")
# print(s.get_name())
# print(s.name)
#
# s.name = "Myrza2"
# print(s.name)
# print(s.age)
# del s.name
# print(s.age)


