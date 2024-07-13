# Creating a password manager using class objects.

class Credentials:
    # initializing the class with our main concerns, (name, password), for collecting credentials.
    def __init__(self):
        # adding an operation passwd, applicable in deleting passwords.
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

    # clear the None output from this function.
    def export_passwords(self, account_name:str) -> str:
        try:
            for account in self.credentials:
                if account_name == account:
                    if account is not None:
                        return f'The credentials associated with the \'{account_name}\' account are:\nUser name: {self.credentials[account]['username']}\nPassword: {self.credentials[account]['password']}\n'
                    else:
                        pass
        except Exception as e:
            print(f'Oops, no credentials found for {account_name}', e)


# Account = Credentials()

# Google = Account.set_credentials('google', 'Erick', 'passCode')
# Email = Account.set_credentials('email', 'EWG', 'email.psc')
# Facebook = Account.set_credentials('facebook', 'Erc', 'FB.pscode')

# Google_passcode = Account.export_passwords('google')
# email_passcode = Account.export_passwords('email')
# facebook_passcode = Account.export_passwords('facebook')

# print(Google_passcode)
# print(email_passcode)
# print(facebook_passcode)


def main():
    print('\nWelcome to your password manager.') 
    print('Enter option 5 to Exit the system.')
    Account = Credentials()
    
    # 
    def exporter(account_name):
    # this function needs to append retrieved credentials from user account search.
        with open('exported_passwords.txt', 'a+') as exported_passwords:
            exported_passwords.write(Account.export_passwords(account_name))
    
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
                    # Can we get the target credential by id and eliminate it?
                    ...
                    
                    
                # fourth option logic, showing saved credentials by user_name.
                
                elif user_input == 4:
                    print('\nwhich account do you want to export saved passwords?\n')
                    try:
                        user_input_account = input('Enter account name: ')
                        if user_input_account is not None:
                            # writing to file with function.
                            exporter(user_input_account)
                            # giving user feedback and confirmation once done.
                            print('exporting....')
                            print('Done, check the file, "exported_passwords.txt"')
                        else:
                            pass
                    except Exception as e:
                        print('An exception occurred while exporting passwords, try again later.\n')
                        print(f'{e}\n')
                        
                
                
                # fifth option logic, exiting the password manager.
                elif user_input == 5:
                    print('\nExiting the password manager...')
                    print('Goodbye 😀\n')
                    break
                
                else:
                    print('\nEnter a valid option. 😑\nEnter numbers between 1 & 5')
            
        except Exception as e:
            print("\nAbnormal input detected")
            print('\nOops there must have been an error during initialization, kindly start over the process :(')
            print('Exited program with error\n')
            
            
            
            
if __name__ == '__main__':
    main()
