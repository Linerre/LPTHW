# dict style
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# this goes in mystuff.py
def apple():
    print("I AM APPLES!")
# this is just a variable
tangerine = "Living reflection of a dream"

# module style
import mystuff
mystuff.apple()
print(mystuff.tangerine)

class MyStuff(object): # define a class

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# class style
thing = MyStuff() # instaniate or create a class, like importing it
thing.apple() # from class MyStuff (now it equals 'thing') import function apple()

print(thing.tangerine)
