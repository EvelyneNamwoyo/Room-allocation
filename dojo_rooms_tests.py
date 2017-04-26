import unittest
from allocate_rooms import Dojo

class TestDojo(unittest.TestCase):
    def setUp(self):
        self.room = Dojo()

    def test_dojo_instance(self):
        self.room = Dojo()
        self.assertIsInstance(self.room, Dojo, msg='The object should be an instance of the `Dojo` class')

    def test_create_room_successfully(self):
        initial_room_count = len(self.room.all_rooms)
        blue_office = self.room.create_room('office', 'blue')
        self.assertTrue(blue_office)
        new_room_count = len(self.room.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_office_with_multiple_rooms_(self):
        initial_room_count = len(self.room.all_rooms)
        office_rooms = self.room.create_room('office','heep','purple','green' )
        self.assertTrue(office_rooms)
        rooms_added = len(self.room.all_rooms)
        self.assertEqual(rooms_added - initial_room_count, 3)

if __name__ == "__main__":
    unittest.main()