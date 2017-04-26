class Room(object):
    def __init__(self, rname):
        self.rname=rname
        self.rtype = __class__.__name__
        self.people_list = []

    def add_person_list(self,pason):
        self.people_list.append(pason)

    def no_people(self):
        return len(self.people_list)
        
class OfficeSpace(Room):
    def __init__(self, rname):
        super(OfficeSpace,self).__init__(rname)
        self.max_no=6
        self.rtype = __class__.__name__
    
    def more_space(self):
        if len(self.people_list) < self.max_no:
            return True

        # Room.__init__(self,rname,rtype,max_no)
class LivingSpace(Room):
    def __init__(self, rname):
        super(LivingSpace,self).__init__(rname)
        self.max_no=4
        self.rtype = __class__.__name__
    def more_space(self):
        if len(self.people_list) < self.max_no:
            return True

        # Room.__init__(self,rname,rtype,max_no)