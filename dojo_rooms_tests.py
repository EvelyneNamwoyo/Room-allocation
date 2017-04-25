import unittest
from allocate_rooms import Dojo

class TestCreateRoomAddRoom(unittest.TestCase):
    def test_create_room_successfully(self):
        my_class_instance = Dojo()
        initial_room_count = len(my_class_instance.room_list)
        blue_office = my_class_instance.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(my_class_instance.room_list)
        self.assertEqual(new_room_count - initial_room_count, 1)
if __name__ == "__main__":
    unittest.main()