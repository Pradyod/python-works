class Shape():

    def __init__(self,name,):

    

    def calculate_area(self):
        print(f"calculating{self.name} area")

class Square():

    def __init__(self,name,edge,count,s):

        super().__init__(name,edge,count)
        self.s=s

    def calculate_area(self):

        a=self.s**2


        print(f"area of {self.name} is {a}")

class Rectangle():

        def __init__(self,name,edge_count,b):

            super().__init__(name,edge_count)
            self.b=b

