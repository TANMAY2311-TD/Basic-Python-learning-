class Keyboard:
    def __init__(self, language, connection):
        self.language = language
        self.connection = connection

    def definition(self):
        print("Keyboard is an input device")

    def numer_of_keys(self):
        print("There are 101 keys")


my_keyboard = Keyboard('English', 'wired')
print(my_keyboard.language)
print(my_keyboard.connection)


#another example of Constructor
class AboutMe:
    def __init__(self, name, age, occupation, id, address):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.id = id
        self.address = address


    def talk(self):
        print(f"My name is {self.name}. I am {self.age} years old. I am a {self.occupation}. "
              f"My ID is: {self.id}. and I am from {self.address}.")


tanmay = AboutMe('Tanmay Das (TD)', '22','student','22010105', 'Chattogram, Bangladesh' )
tanmay.talk()
