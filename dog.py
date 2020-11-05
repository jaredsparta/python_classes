class Dog:
    # This is a class variable
    animal_kind = "Canine"
    def __init__(self, name):
        self.name = name

    def bark(self):
        # Calling this function, changes the class variable
        self.animal_kind = "Fish"
        return "woof!"

jeff = Dog("Jeff")

print(jeff.animal_kind)
jeff.bark()
print(jeff.animal_kind)

fido = Dog("Fido")
print(fido.animal_kind)

