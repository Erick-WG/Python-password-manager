# Creating a password manager using class objects.
from helper_functions.number_checker import is_number

class Credentials:
    # initializin the class with our main concerns, (name, password), for collecting credentials.
    def __init__(self):
        self.credentials = {}
        
    # creating new credentials and storing them in a list.
    def set_credentials(self, account,user_name, password):
        # creation
        self.credentials[account] = {'username':user_name, 'password':password}  
    
    def get_credentials(self, account_name):
        if account_name in self.credentials:
            pass_code = self.credentials[account_name]['password']
            return f'\nPassword for {account_name} is: {pass_code}\n'
        else:
            return f'\nNo credentials found for: {account_name}\n'
                
        


# Account = Credentials()

# Google = Account.set_credentials('google', 'Erick', 'passCode')
# # Email = Account.set_credentials('email', 'EWG', 'email.psc')
# # Facebook = Account.set_credentials('facebook', 'Erc', 'FB.pscode')

# Google_passcode = Account.get_credentials('google')
# # email_passcode = Account.get_credentials('email')
# # facebook_passcode = Account.get_credentials('facebook')

# print(Google_passcode)
# # print(email_passcode)
# # print(facebook_passcode)



def main():
    print('\nWelcome to your password manager.')    
    Account = Credentials()
    while True:
        print('kindly select an option you wish to continue with.\n')
        # creating user options and displaying them to the user.
        options = {1:'Save a password', 2:'Get saved password by account name', 3:'Delete saved password', 4:'Exit password manager'}
        
        for option in options:
            print(f'{option}: {options[option]}')
        
        # collecting the user input for the logic.
        try:
            user_input = int(input("Which option number do you wish to continue with? "))
            
        except ValueError:
            print("\nAbnormal input detected")
            user_input = int(input("Which option number do you wish to continue with? "))
            
            # verifying the second input is really a number.
            if user_input == is_number(user_input):
                continue
            else:
                print('\nOoops there must have been an error during initialization, kindly start over the process :(')
                print('Exited program with error\n')
                break
            
        try:
            if user_input  == 1:
                print('\nFollow the prompts to save a new password')
                account_name = input("Account name: ")
                user_name = input("user name: ")
                password = input("password: ")
                
                # creating the credentials and storing them in our object/ dictionary.
                _ = Account.set_credentials(account_name, user_name, password)
                # success message
                print(f'\nsuccessfully created and saved credentials for your {account_name} account\n')
                
            elif user_input == 2:
                print('\nWhat is the name of the account you need saved password for? ')
                account_name = input("Account name: ")
                ps_d = Account.get_credentials(account_name)
                print(f'successfully fetched password for {account_name}\n')
                print(f'{ps_d}')
                
                
            elif user_input == 4:
                print('\nExiting the password manager...')
                print('Goodbye 😀')
                break
            
        except Exception as e:
            print('\nOoops there must have been an error during initialization, kindly start over the process :(')
            print('Exited program with error\n')
            
            
            
            
if __name__ == '__main__':
    main()