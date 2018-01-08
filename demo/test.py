
class Animal(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print("this is destroy")

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score=score

c = Animal('gao',23)
print(c.name)
c.score = 100
print(c.score)

