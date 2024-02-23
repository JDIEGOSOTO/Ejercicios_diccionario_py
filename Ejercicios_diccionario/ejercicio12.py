class SocialNetworkAnalisis():
    def __init__(self):
        self.accounts = {}
    
    def add_account(self):
        account_id = str(len(self.accounts) + 1)
        nombre = input("Type the name of the account: ")
        number_of_followers = int(input("Type the number of followers: "))
        self.accounts[account_id] = { "name" : nombre, "followers" : number_of_followers}

    def show_accounts(self):
        print("List of accounts: ")
        for id, account in self.accounts.items():
            print(f"Account {id}: ")
            account_info = f"Name: {account["name"].title()}, Number of Followers: {account["followers"]}"
            print(account_info)

account1 = SocialNetworkAnalisis()
account1.add_account()
account1.show_accounts()