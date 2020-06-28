import unittest  # import unittest class
from credential import Credential  # import the Credential class


class TestCredential(unittest.TestCase):
    '''
     Test class that defines test cases for the user class behaviours

    Arg: 
        unittest.testCase : Testcase class that helps in creating test cases
    '''

    new_credential = Credential("username")

    def setup(self):
        '''
        setup method to run before each test runs
        '''
        self.new_credential = Credential("username")
    
    def tearDown(self):
        '''
        tearDown: method that runs after each test to clear the dictionary
        '''
        Credential.credential_dict = {}

    def test_init(self):
        '''
        test_init: Unit test case to test if Credential object is initialized properly
        '''
        self.assertEqual(self.new_credential.username, "username")

    def test_save_credential(self):
        '''
        test_save_credential: Unit test that test saving a credential to the dictionary
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_dict), 1)

    def test_add_credential(self):
        '''
        test_add_credential: Unit test that add a credential to the dictionary for the user
        '''
        self.new_credential.add_site_credential("website", "sitepassword")
        self.assertEqual(len(Credential.credential_dict), 1)


if __name__ == '__main__':
    unittest.main()
