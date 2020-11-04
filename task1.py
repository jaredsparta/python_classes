#task 1

class Cat:
    has_whiskers = True
    jumping_ability = 10

    def __init__(self, name):
        self.name = name

    def meow(self):
        return "Meow"


Molly = Cat("Molly")
Felix = Cat("Felix")
Smudge = Cat("Smudge")

# They all have the same class variables as they are not instance-specific
for cat in (Molly, Felix, Smudge):
    print( f"{cat.name} has whiskers: {cat.has_whiskers} and has a jumping ability of {cat.jumping_ability}")


# Changing the class variables in each instance:
Molly.jumping_ability = 5 # She can't jump that well
Felix.jumping_ability = 15 # He can jump really high
Smudge.jumping_ability = 1 # They broke their leg recently

Molly.has_whiskers = False # No whiskers

print("")
# Now everyone has different attributes making them all special in their own way
for cat in (Molly, Felix, Smudge):
    print( f"{cat.name} has whiskers: {cat.has_whiskers} and has a jumping ability of {cat.jumping_ability}")