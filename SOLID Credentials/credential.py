# Main classes to manage credentials


# Credentials class to instantiate the credentials object.
from dataclasses import dataclass

@dataclass
class Credential:
    credential: dict

# Sub class to create credentials
class builder (Credential):
    def __init__(self, user_name, account_name, password):
        super().__init__(credential={})
        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        # self.credential = credential

    # Build_func
    def build (self):
        self.credential[self.user_name] = {'account':self.account_name, 'user_name':self.user_name, 'password':self.password}


    # Read_func
    def read (self, user_name) -> str:
        try:
            for user_name in self.credential:
                if user_name in self.credential:
                    pass_code = self.credential[user_name]['password']
                    return f'Password for {user_name} is: {pass_code}\n'
                else:
                    return f'\nNo credentials found for: {user_name}\n'
        except Exception as e:
            print(f"We apologize for the malfunction, an exception occurred: {e}")



# Sub class to Read credentials created
# Sub class to Update credentials created
# Sub class to Delete credentials created
# sub class to export credentials created by search and export.




# Testing and debugging.

account_name = 'Google'
user_name = 'Erick'
password = 'p455w0rd'

account = builder(user_name, account_name, password)

print(f'{account.account_name} {account.user_name} {account.password}', sep=" | ")

try:
    get_account = account.read(user_name)
    print(get_account)
except Exception as e:
    print(f"An error: {e} occurred")