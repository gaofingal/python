class Animal(object):

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary
    @salary.deleter
    def salary(self):
        del self.__salary
        print("this is delete")


a = Animal()
a.salary=1000
print(a.salary)
del a.salary
