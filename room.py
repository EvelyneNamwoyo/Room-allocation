class Room(object):
    def __init__(self, rname, rtype, max_no):
        self.max_no = max_no
        self.rtype =rtype
        self.rname=rname
class OfficeSpace(Room):
    def __init__(self, rname):
        max_no=6
        rtype='Office'
        Room.__init__(self,rname,rtype,max_no)
class LivingSpace(Room):
    def __init__(self, rname):
        max_no=4
        rtype='Living Space'
        Room.__init__(self,rname,rtype,max_no)