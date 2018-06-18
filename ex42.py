class Animal(object):
    pass

<<<<<<< HEAD
 
class Dog(Animal):

    def __init__(self, name):
        
        self.name = name


class Cat(Animal):

    def __init__(self, name): 
         
        self.name = name

 
class Person(object):

    def __init__(self, name): 
        
        self.name = name


        self.pet = None


class Employee(Person):

    def __init__(self, name, salary): 
         
        super(Employee, self).__init__(name) 
         
        self.salary = salary


class Fish(object): 
    pass


class Salmon(Fish): 
    pass

=======
class Dog(Animal):

    def __init__(self, name):
        self.name = name

class Cat(Animal):

    def __init__(self, name):

        self.name = name

class Person(object):

    def __init__(self, name):

        self.name=name
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):

        super(Employee, self).__init__(name)

        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass
>>>>>>> dbdda2f3513d8576d9b1c9fd65f2d1bc633390b3

class Halibut(Fish):
    pass

<<<<<<< HEAD


rover = Dog("Rover")
 
satan = Cat("Satan")

 
mary = Person("Mary")

 
mary.pet = satan


frank = Employee("Frank", 120000)


frank.pet = rover

flipper = Fish()


crouse = Salmon()

 
=======
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan
    

frank = Employee("Frank", 120000)
    

frank.pet = rover
    

flipper = Fish()

crouse = Salmon()

>>>>>>> dbdda2f3513d8576d9b1c9fd65f2d1bc633390b3
harry = Halibut()
