class Parent:

    def car(self):

        print("parent Swift car")

    def bike(self):

        print("parent Passion pro")

class Child(Parent):

    def bike(self):
        
        print("child trimpuh bike")

child_instance=Child()

child_instance.bike()

child_instance.car()