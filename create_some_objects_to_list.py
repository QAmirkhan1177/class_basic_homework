from create_one_attribute import Person

#Create an object named "p1" whose name is "Anvar"
#Create an object named "p2" whose name is "Shavkat"
#Create an object named "p3" whose name is "Jasur"

#Add these objects to the "persons" named list
class Person:
    def __init__(self,p1,p2,p3) -> None:
        self.p1=p1
        self.p2=p2
        self.p3=p3
Ali=Person()