# Creating a password manager using class objects.

class Credentials:
    # initializin the class with our main concerns, (name, password), for collecting credentials.
    def __init__(self):
        self.credentials = {}
        
    # creating new credentials and storing them in a list.
    def set_credentials(self, account,user_name, password):
        # creation
        self.credentials[account] = {user_name: password}  
    
    def get_credentials(self, account_name):
        if account_name in self.credentials:
            pass_code = self.credentials[account_name]
            return f'Password for {account_name} is {pass_code}'
        else:
            return f'No credentials found for {account_name}'
                
        


# class PasswordManager(Credentials):
#     pass

Account = Credentials()

Google = Account.set_credentials('google', 'Erick', 'passCode')
Email = Account.set_credentials('email', 'EWG', 'email.psc')
Facebook = Account.set_credentials('facebook', 'Erc', 'FB.pscode')

Google_passcode = Account.get_credentials('google')
email_passcode = Account.get_credentials('email')
facebook_passcode = Account.get_credentials('facebook')

print(Google_passcode)
print(email_passcode)
print(facebook_passcode)