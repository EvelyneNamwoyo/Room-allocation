import random
from room import OfficeSpace
from room import LivingSpace
from room import Room
from person import Staff
from person import Fellow


class Dojo(object):

    def __init__(self):
        self.people = []
        self.persons = []
        self.all_rooms = []
        self.rooms = []
        self.office_rooms = []
        self.living_rooms = []
        self.free_rooms = []
        self.people_with_rooms = {}
        self.people_added = []
        self.fellows = []
        self.staff = []

        """ this function creates a room of either office or living space, and appends 
        the created room to a list of rooms"""

    def create_room(self, rtype, *rname):
        # rtype = rtype.lower()
        room_name = []
        if rtype == 'office':
            for oname in rname:
                if oname in room_name:
                    return 'Sorry office name exists'
                else:
                    room_name.append(oname)
                    office = OfficeSpace(oname)
                    self.rooms.append(office)

                    print('An office called ' + office.rname +' has been successfully created!')

                self.office_rooms.append(office)
        elif rtype == 'livingspace':
            for oname in rname:
                living = LivingSpace(oname)
                self.rooms.append(living)
                print(living.rname)
                self.living_rooms.append(living)

        return self.all_rooms
    """This function adds a person to a room, and randomly allocates the to available office space or living space"""

    def add_person(self, pname, gender, position,wants_accommodation=False):
        if position == 'staff':
            pa = Staff(pname, gender, position)
            self.people_added.append(pa)
            self.staff.append(pa)
            # check whether person has already been added
            print(self.people_added)
            random_room = self.select_random_room(self.office_rooms)
            random_room.add_person_list(pa)
            # return random_room.people_list
            print('hahah')
            print(position + ' ' + pname + ' has been successfully added')
            print(pname + ' has been allocated the office ' + random_room.rname)
        else:
            pa = Fellow(pname, gender)
            self.people_added.append(pa)
            self.fellows.append(pa)
            random_room = self.select_random_room(self.office_rooms)
            random_room.add_person_list(pa)
            if wants_accommodation == 'Y':
                random_room = self.select_random_room(self.living_rooms)
                random_room.add_person_list(pa)
            print(position + ' ' + pname + ' has been successfully added')
            print(pname + ' has been allocated the office ' + random_room.rname)

    """this function randomly selects an empty room and returns the name of the room"""

    def select_random_room(self, room_lis):

        for room in room_lis:
            if room.room_has_space():
                self.free_rooms.append(room)
        return random.choice(self.free_rooms)

    def print_room(self, name):
        specific_room = [room for room in self.rooms if name == room.rname][0]
        # print(specific_room.people_list)
        for pips in specific_room.people_list:
            return pips.pname

    def print_allocations(self, txt = ""):
        output = ''
        for room in self.rooms:
            print("People in " + room.rname)
            output += 'People in ' + room.rname + '\n'
            for r in room.people_list:
                print (r.pname)
                output += r.pname + '\n'

        if txt == '':
            print (output)
        else:
            a = open(txt, 'w+')
            a.write(output)
            a.close()

            # if len(room.people_list) > 0:
                # self.people_with_rooms[room.rname] = room.people_list.pname
        # print (self.people_with_rooms)
"""this functions prints the people who have been added but not yet allocated to rooms"""
*
    def print_unallocted(self, txt=''):
        lis = Room()
        a = (set(self.people_added) - set(lis.people_list))
        new_list = list(a)
        for i in new_list:
            print (i.rname)
        # for people in self.people_added:
        #     print(people)
        #     # if people not in people.people_list:
        #     #     return people.pname


    """thie function reallocates a person to a new roo"""
    def reallocate_rooms(self, person_identifier, new_room_name):
        # first search to see if the room to be reallocated to exists
        rooms = []
        new_room = None
        for room in self.rooms:
            rooms.append(room.rname)
        if new_room_name.lower() not in rooms:
            print('That room doesnt exist')

        #check for extra space in new room
        for room in self.rooms:
            if new_room_name.lower() == room.rname:
                new_room = room
        if new_room.room_has_space():
            former_room = None
            person_name = None


    def load_peploe(txt):
        


a=Dojo()
print (a.create_room('office', 'gordy','green', 'purple'))
print(a.add_person('e', 'female', 'staff'))
print(a.add_person('mahad', 'female', 'staff'))
print(a.add_person('eve', 'female', 'staff'))
print(a.add_person('ev', 'female', 'staff'))
# print(a.add_person('Staff', 'female', 'Mahad'))
# print(a.add_person('Staff', 'female', 'jack'))
# print(a.add_person('Staff', 'female', 'had'))
a.add_person('Eva', 'female', 'staff')
print (a.print_room('gordy'))
print (a.print_allocations('test.txt'))
# print(a.print_allocations())


