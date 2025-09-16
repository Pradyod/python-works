class Superhero():

    name:str
    city:str
    superpowers:str
    affliation:str

    def set_superhero(self,name,city,superpowers,affliation):

        self.name=name
        self.city=city
        self.superpowers=superpowers
        self.affliation=affliation

    def display_superhero(self):

        print(self.name,self.city,self.superpowers,self.affliation)

sup_instance1=Superhero()
sup_instance2=Superhero()

sup_instance1.set_superhero("Batman","Gotham City","Detective Skills","Justice League")
sup_instance1.display_superhero()