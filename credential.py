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

    def save_credential(self):
        '''
        save_credential: Method that saves a new credential to the dictionary
        '''
        Credential.credential_dict["name"] = "username"

    def add_site_credential(self, site, password):
        '''
        add_site_credential: Method that add a site redential to the dictionary

        Args: 
            site: website to be added
            password: password to the website
        '''
        Credential.credential_dict[site] = password

    def delete_credential(self, cred_name):
        '''
        delete_credential: Method that deletes the last credential saved to the dictionary
        '''
        Credential.credential_dict.pop(cred_name)

    @classmethod
    def find_credential(cls, cred_name):
        '''
        find_credential: Method that checks if a credential exists
        '''
        if cred_name in cls.credential_dict:
            return True

    @classmethod
    def display_credentials(cls):
        '''
        display_credentials: Class method that returns all credentials in the dictionary
        '''
        return cls.credential_dict
