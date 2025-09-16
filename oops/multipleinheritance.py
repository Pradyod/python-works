class Father():

    def cricket_skills(self):

        print("father cricket skills")

    def cooking_skills(self):

        print("father cooking skills")

class Mother():


    def cooking_skills(self):

        print("father cooking skills")

class Child(Father,Mother):

    def learning_skills(self):
        
        print("child learning skills")

child_instance=Child()

child_instance.learning_skills()

child_instance.cooking_skills()

child_instance.cricket_skills()