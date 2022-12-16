# Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - 
# который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в 
# случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

class Soup:
    def __init__(self, name, main_ingr = ''):
        self.main_ingr = main_ingr
        self.name = name
    
    def show_my_soup(self):
        if self.main_ingr == '': print(f'{self.name} is just hot water')
        else: print(f'{self.name} - {self.main_ingr}')

cabbage_soup = Soup('Cabbage soup','cabbage')
doshirak = Soup('Doshirak')

cabbage_soup.show_my_soup()
doshirak.show_my_soup()