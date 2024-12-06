from models import Account

class Bot:
    def __init__(self, account: Account):
        self.account = account
        self.browser = Browser(account)
        self.metamask = Metamask(account)
        self.exchange = Exchange(account)


class Browser:

    def __init__(self, account: Account):
        self.account = account


    def open_browser(self):
        print(f'Open browser with account: {self.account.profile_number}')


    def close_browser(self):
        print(f'Close browser with account: {self.account.profile_number}')

    def open_url(self, url: str):
        print(f'{self.account.profile_number} Open url: {url}')


class Metamask:
    def __init__(self, account: Account):
        self.account = account

    def auth(self):
        print(f'{self.account.profile_number} Auth in Metamask with account: {self.account.password}')

    def sent_tx(self):
        print(f'{self.account.profile_number} Sent tx from Metamask, {self.account.address}')

class Exchange:
    def __init__(self, account: Account):
        self.account = account


    def withdraw(self, token: str, amount: float):
        print(f'{self.account.profile_number} Withdraw {amount} {token} from exchange {self.account.address}')