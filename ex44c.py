class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def alterde(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
