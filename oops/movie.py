class Movie():

    def __init__(self,name,year,language,director):
        self.name=name
        self.year=year
        self.language=language
        self.director=director

    def display_movie(self):

        print(self.name,self.year,self.language,self.director)

    def __str__(self):
        return self.name    
    
movie_intstance=Movie("Batman",2006,"English","Nolan")

movie_intstance.display_movie()

print(movie_intstance)