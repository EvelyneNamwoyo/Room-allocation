from room import OfficeSpace
from room import LivingSpace
from person import Staff
from person import Fellow
class Dojo(object):

    def __init__(self):
        self.people=[]
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


    def add_person(self,pname,position,gender):
        persons=[]
        if position == 'Staff':
            pers = Person(pname,gender)
            persons.append(pers)
            for i in persons.pname:
                print (i)






a=Dojo()
a.add_person('eva','Staff','female')
print (a.create_room('LivingSpace','gordy','kjj','ll'))