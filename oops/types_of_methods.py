class Employee:
    #instancemethod
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display_employee(self):

        print(self.id,self.name)

    @classmethod
    def cls_method_demo(cls):

        print("inside class method")

    @staticmethod
    def cls_static_method():
        print("inside static method")
    
Employee.cls_method_demo()
Employee.cls_static_method()