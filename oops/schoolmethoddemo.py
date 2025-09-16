class Student:

    school_name="ABC"

    def __init__(self,rol,name,total):

        self.rol=rol
        self.name=name
        self.total=total

    @classmethod
    def update_school_name(cls,new_school_name):
        cls.school_name=new_school_name
        print(cls.school_name)

    @staticmethod
    def is_pass(total):

        return True if total>140 else False
    
Student_instance1=Student(1000,"hari",123)
Student_instance2=Student(1001,"adi",153)

Student.update_school_name("cms")

print(Student.is_pass(Student_instance1.total))
        