class Laptop:
    def parts(self):
        print('Laptop: Mouse, Keyboard, Display, Motherboard')

my_laptop = Laptop()
my_laptop.parts()


class Desktop:
    def parts(self):
        print('Desktop: Mouse, Keyboard, Display, Motherboard')

my_desktop = Desktop()
my_desktop.parts()


#Laptop: parent and Desktop: child
class Desktop_C(Laptop):
    def weight(self):
        print('Desktops are heavy-weight')

my_desktop = Desktop_C()
my_desktop.parts()
my_desktop.weight()
