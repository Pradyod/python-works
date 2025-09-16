class Book():

    def __init__(self,name,author,price):

        self.name=name
        self.author=author
        self.price=price

    def display_book(self):

        print(self.name,self.author,self.price)


book_int=Book("GoatLife","Benyamin",560)

book_int.display_book()
        