from room import OfficeSpace
from room import LivingSpace
class Dojo(object):

    def __init__(self):
        self.all_rooms = []
        self.rooms = []

    def create_room(self, rtype, *rname):
        
        if rtype is 'office':
            office = OfficeSpace(rname)
            self.rooms.append(office)
            tuple_rooms = office.rname
            for room in tuple_rooms:
                self.all_rooms.append(room)

        elif rtype is 'LivingSpace': 
            living = LivingSpace(rname)
            self.rooms.append(living)
            tuple_rooms = office.rname
            for room in tuple_rooms:
                self.all_rooms.append(room)

        return True


a=Dojo()
print (a.create_room('office','gordy','kjj','ll'))