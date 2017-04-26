from room import OfficeSpace
from room import LivingSpace
class Dojo(object):

    def __init__(self):
        self.all_rooms = []
        self.rooms = []

    def create_room(self, rtype, *rname):
        
        if rtype == 'office':
            office = OfficeSpace(rname)
            self.rooms.append(office)
            tuple_rooms = office.rname
            for room in tuple_rooms:
                self.all_rooms.append(room)

        elif rtype == 'LivingSpace': 
            living = LivingSpace(rname)
            self.rooms.append(living)
            tuple_rooms = living.rname
            for room in tuple_rooms:
                self.all_rooms.append(room)

        return self.all_rooms
    # def add_person()


a=Dojo()
print (a.create_room('LivingSpace','gordy','kjj','ll'))