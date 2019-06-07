badges = {}


class Badge:
    def __init__(self, badgeid, doors):
        self.badgeid = badgeid
        self.doors = doors

    def __repr__(self):
        return f"The badge ID is: {self.badgeid}, it can access doors: {self.doors}."


class BadgeRepo:
    def create_badge(self, badgeid, doors):
        badges.update({badgeid: doors})

    def view_badges(self):
        print(badges)
        return badges

    def add_door(self, badgeid, new_door):
        for i in badges:
            if badgeid == i.badgeid:
                i.doors.update(new_door)
                return True

    def delete_door(self, badgeid, dor):
        for i in badges:
            if badgeid == i.badgeid:
                for x in i.doors:
                    if dor == x:
                        z = i.doors.index(x)
                        i.doors.popitem(z)
                        return x
        else:
            return

    def delete_badge(self, badgeid):
        for i in badges:
            if badgeid == i.badgeid:
                x = badges.index(i)
                badges.popitem(x)
                return True


# x = Badge(2, 3)
# print(x)

#The logic works, look at other notes in the ui file. #
