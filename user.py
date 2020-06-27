class User:

    '''
    Model class for application user. The user is created in constructor. 
    The user is persisted to disk in a plain text file

    Params:
        name: username used by user to login into application
        password: password oser to application
    '''

    user_list = []  # empty user list

    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties for our objects
        Args:
                username: New user's username
                password: New user's password
        '''
        self.username = username
        self.password = password
    
    def save_user(self):
        '''
        save_user method: saves user to user list as an append
        '''
        User.user_list.append(self)
