class Person(object):
    def __init__(self, pname, position, gender):
        self.pname = pname
        self.position = position

class Staff(Person):
    def __init__(self, pname,gender):
        position = 'staff'
        Person.__init__(self,pname,position,gender)

class LivingSpace(Person):
    def __init__(self, pname,gender):
        position = 'fellow'
        Person.__init__(self,pname,position,gender)