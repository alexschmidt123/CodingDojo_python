from numpy import False_
import parent
pet1 = parent.Pet("Simon", "Hedgehog", True)
dog1 = parent.Dog("Chilli", "Hustky", False)

# pet1.sleep().display().eat().display().play().display().noise()
print(__name__)

ninja1 = parent.Ninja("Joseph", "Josetha", "bacon", "banana", pet1)
# ninja1.walk().feed().bathe()

dog1.sleep().display().eat().display().play().display().barking()