
credentials = {'google': {'username': 'erick', 'password': '1234'}}

def mock_data(account_name):
    for account in credentials:
            if account_name == account:
                # print (f'The credentials associated with the \'{account_name}\' account are:\nUser name: {self.credentials[account]['username']}\nPassword: {self.credentials[account]['password']}\n')
                return f'The credentials associated with the \'{account_name}\' account are:\nUser name: {credentials[account]['username']}\nPassword: {credentials[account]['password']}\n'


def exporter(account_name):
    # this function needs to append retrieved credentials from user account search.
    with open('exported_passwords.txt', 'w') as exported_passwords:
        exported_passwords.write(mock_data(account_name))
    
    
print('which account do you want to export saved passwords?')
try:
    user_input_account = input('Enter account name: ')
    if user_input_account:
        # writing to file with function.
        exporter(user_input_account)
        # giving user feedback and confirmation once done.
        print('exporting....')
        print('Done, check the file, "exported_passwords.txt"')
except Exception as e:
    print('An exception occurred while exporting passwords, try again later.\n')
    print(e)