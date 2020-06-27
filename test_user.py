import unittest  # import unit testing module
from user import User  # import the user class


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours

    Arg: 
        unittest.testCase : Testcase class that helps in creating test cases
    '''

    new_user = User("testuser", "testpassword")

    def setup(self):
        '''
        Seup method to run before each test case
        '''
        self.new_user = User(
            "testuser", "testpassword")  # create new contact object

    def tearDown(self):
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_user.username, "testuser")
        self.assertEqual(self.new_user.password, "testpassword")

    def test_save_user(self):
        '''
        test_save_user test case - tests if a user is saved in the user_list array
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
    
    def test_save_multiple_user(self):
        ''' 
        test_save_multiple_user test case tests if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("testuser1", "testpassword1")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
    
    def test_delete_user(self):
        '''
        test_delete_user test case tests if we can delete a user from the user_list array
        '''
        self.new_user.save_user()
        test_user = User("testuser2", "testpassword2")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)
    
    def test_find_by_name(self):
        '''
        test_find_user_by_name: Unit test to see if you can search for user by name and display details
        '''
        self.new_user.save_user()
        test_user = User("testuser2", "testpassword2")
        test_user.save_user()

        found_user = User.find_by_name("testuser2")
        self.assertEqual(found_user.password, test_user.password)

    def test_user_exists(self):
        '''
        test_user_exists: Unit test that returns boolean if a contact exists in the user list
        '''
        self.new_user.save_user()
        test_user = User("testuser1", "testpassword1")
        test_user.save_user()

        user_exists = User.user_exist("testuser1")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
