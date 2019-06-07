class Menu:

    def __init__(self, idnum, name, desc, ingredients, price):
        self.idnum = idnum
        self.name = name
        self.desc = desc
        self.ingredients = ingredients
        self.price = price

    def __repr__(self):
        return self.name


class MenuRepo:

    def __init__(self):
        self.menulist = []

    def add_item(self, idnum, name, desc, ingredients, price):

        new = Menu(idnum, name, desc, ingredients, price)
        self.menulist.append(new)

    def delete_menu_item(self, name):
        for item in self.menulist:
            if name == item.name:
                index = self.menulist.index(item)
                del self.menulist[index]
                return True

    def view_menu(self):
        return self.menulist
