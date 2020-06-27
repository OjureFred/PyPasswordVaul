class Credential:
    '''
    Model class for application user credentials. The credential is created in constructor. 
    The credential can be persisted to disk in a plain text file

    Params:
        name: username used by user to store web credentials
        hotmail: user password for  hotmail.com
        twitter: user password for twitter.com
        facebook: user password for facebook.com
        instagram: user password to instagram

        example of a credential dictionary
        credential_dict {
            'username': 'user1,
            'hotmail': 'password1',
            'twitter': 'password2',
            'facebook': 'password3',
            'instagram': 'password4',
            'google': 'password5'
        }

    '''

    credential_dict = {}  # empty credentials list

    def __init__(self, username):
        self.username = username
        self.hotmail = ''
        self.twitter = ''
        self.facebook = ''
        self.instagram = ''
        self. google = ''
