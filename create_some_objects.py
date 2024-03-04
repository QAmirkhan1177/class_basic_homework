from create_one_attribute import Person

#create an object named "p1" whose name is "Anvar"
#create an object named "p2" whose name is "Shavkat"
class Person:
    def __init__(self,p1,p2) -> None:
        self.p1=p1
        self.p2=p2
name=Person("Said","Anvar")