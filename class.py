class Cat:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says: {self.sound}")


cat = Cat("Chiku", "meow...meow..")

cat.speak()

class Pet(Cat):
  def __init__(self,name,sound):
    super().__init__(self,name,sound)
my_pet = pet()
