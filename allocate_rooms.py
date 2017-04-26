import random
from room import OfficeSpace
from room import LivingSpace
from person import Staff
from person import Fellow
class Dojo(object):

    def __init__(self):
        self.people = []
        self.persons = []
        self.all_rooms = []
        self.rooms = []
    """ this function creates a room of either office or living space, and appends the created room to a list rooms"""
    def create_room(self, rtype, *rname):
        if rtype == 'Office':
            for oname in rname:
                office = OfficeSpace(rname)
                self.rooms.append(office)
                print(office.rname)
            #tuple_rooms = office.rname
            #for room in tuple_rooms:
                self.all_rooms.append(office)

        elif rtype == 'LivingSpace': 
            living = LivingSpace(rname)
            self.rooms.append(living)
            tuple_rooms = living.rname
            for room in tuple_rooms:
                self.all_rooms.append(room)

        return self.all_rooms
    """This function adds a person to a room, an drandomly allocates the to availble office or space"""

    def add_person(self,position,gender,pname):
        if position == 'Fellow' and self.accommodation == True:
            pa = Fellow(pname,gender)
        else:
            pa = Staff(pname,gender)

        free_rooms = []
        for room in self.rooms:
            if room.more_space():
                room.add_person_list(pa)
                for pips in room.people_list:
                    return pips.pname
                for i in room.rname:
                    free_rooms.append(i)
            a=random.choice(free_rooms)
            print (a)
        # print(room.people_list[0].pname)
                # for frooms in room.rname:
                    # free_rooms.append(frooms)

    #     

    #         return(free_rooms)
    # def add_person(self,position,gender,pname):
    #     if position == 'Fellow' and self.accommodation == True:
    #             free_rooms
                # if position == 'Fellow' and accommodation == True:
                #     room.add_people_list(room.pname)
                #     free_rooms.append(room.)


        
        # if position == 'Staff':
        #     pers = Staff(pname,gender)
        #     self.persons.append(pers)
        #     self.people.append(pers.pname)
        # return True
    # def allocate_room(self):
    #     allocate={}
    #     if self.position == 'Staff': 
    #         for room in self.rooms:
    #                 if room.rtype == 'Office':
    #                     allocate[room.rname] = add_person(self,position,gender,pname)
    #     print (allocate)








a=Dojo()
print (a.create_room('Office','gordy','hh','uyt'))
print(a.add_person('Office','female','eva'))

