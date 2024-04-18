# Creating a password manager using class objects.

class Credentials:
    # initializin the class with our main concerns, (name, password), for collecting credentials.
    def __init__(self):
        # adding an operation paswd, applicable in deleting passwords.
        self.credentials = {}
        
    # creating new credentials and storing them in a list.
    def set_credentials(self, account,user_name, password):
        # creation
        self.credentials[account] = {'username':user_name, 'password':password}  
    
    def _get_credentials(self, account_name):
        if account_name in self.credentials:
            pass_code = self.credentials[account_name]['password']
            return f'Password for {account_name} is: {pass_code}\n'
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
    print('Enter option 5 to Exit the system.')
    Account = Credentials()
    while True:
        print('Select an option you wish to continue with.\n')
        # creating user options and displaying them to the user.
        options = {1:'Save a password', 2:'Get saved password by account name', 3:'Delete saved password', 4:'Show saved passwords',5:'Exit password manager'}
        
        for option in options:
            print(f'{option}: {options[option]}')
            
            
        try:
            # collecting the user input for the logic.
            user_input = int(input("\nWhich option number do you wish to continue with? "))
           
            # verifying the second input is really a number.
            if user_input.is_integer:
                
                # first option logic, creating credentials.
                if user_input  == 1:
                    print('\nFollow the prompts to save a new password\n')
                    account_name = input("Account name: ")
                    user_name = input("user name: ")
                    password = input("password: ")
                    
                    # creating the credentials and storing them in our object/ dictionary.
                    Account.set_credentials(account_name, user_name, password)
                    # success message
                    print(f'\nsuccessfully created and saved credentials for your {account_name} account\n')
                    
                # second option logic, looking up credentials.
                elif user_input == 2:
                    print('\nSearch for password by account name.\n')
                    account_name = input("Enter account name: ")
                    ps_d = Account.get_credentials(account_name)
                    print(f'\nsuccessfully fetched password for {account_name}')
                    print(f'{ps_d}')
                    
                # third option logic, Deleting credentials.
                elif user_input == 3:
                    # deleting account credentials.
                    ...
                    
                    
                # fourth option logic, showing saved credentials by user_name.
                
                
                # fifth option logic, exiting the password manager.
                elif user_input == 5:
                    print('\nExiting the password manager...')
                    print('Goodbye 😀\n')
                    break
                
                else:
                    print('\nEnter a valid option. 🙄😑\n')
            else:
                print('\nEnter integer values only😑')
                continue
            
        except Exception as e:
            print("\nAbnormal input detected")
            print('\nOoops there must have been an error during initialization, kindly start over the process :(')
            print('Exited program with error\n')
            
            
            
            
if __name__ == '__main__':
    main()
