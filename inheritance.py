class Dad:
    def football(self):
        print('Dad like watching football')
class Mum:
    def cooking(self):
        print('Mum like cooking')
class Boy (Dad):
    def boy_age(self):
        print("I'm 20 years old")
my_boy=Boy()
my_boy.boy_age()
my_boy.football()
class Girl (Mum):
    def girl_hobby(self):
        print("The girl loves to dance")
the_girl=Girl()
the_girl.cooking()
the_girl.girl_hobby()

