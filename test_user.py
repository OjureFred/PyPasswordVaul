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

if __name__ == '__main__':
    unittest.main()
