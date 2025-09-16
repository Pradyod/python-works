class Student:
    id:int
    name:str
    age:int
    
    def set_student(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    
    def display_student(self):
        print(self.id,self.name,self.age)


std_instance1=Student()
std_instance2=Student()

std_instance1.set_student(1001,"Adil",20)
std_instance1.display_student()