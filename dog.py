class Dog:
    # This is a class variable
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.animal_kind = "Canine"

    def bark(self):
        # Calling this function, changes the class variable
        self.animal_kind = "Fish"
        return "woof!"

jeff = Dog("Jeff", "white")

print(jeff.animal_kind)
jeff.bark()
print(jeff.animal_kind)

fido = Dog("Fido", "brown")
print(fido.name)
