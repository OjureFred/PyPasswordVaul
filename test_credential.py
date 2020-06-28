import unittest  # import unittest class
from credential import Credential  #import the Credential class

class TestCredential(unittest.TestCase):
    '''
     Test class that defines test cases for the user class behaviours

    Arg: 
        unittest.testCase : Testcase class that helps in creating test cases
    '''

    def setup(self):
        '''
        setup method to run before each test runs
        '''
        self.new_credential = Credential("username")

    def test_init(self):
        '''
        test_init: Unit test case to test if Credential object is initialized properly
        '''
        self.assertEqual(self.new_credential.username, "username")
    
    def test_save_credential(self):
        

    
    if __name__ == '__main__':
        unittest.main()