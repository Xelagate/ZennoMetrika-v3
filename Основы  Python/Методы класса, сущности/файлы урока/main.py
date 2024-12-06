from models import Account
from utils import get_list_from_file
from core import Bot


profile_numbers = get_list_from_file('config/profile_numbers.txt')
passwords = get_list_from_file('config/passwords.txt')
private_keys = get_list_from_file('config/private_keys.txt')
addresses = get_list_from_file('config/addresses.txt')

account_for_works = []

for i in range(len(profile_numbers)):
    account = Account(profile_numbers[i], passwords[i], private_keys[i], addresses[i])
    account_for_works.append(account)

for account in account_for_works:
    bot = Bot(account)
    bot.browser.open_browser()
    bot.browser.open_url('https://google.com')
    bot.metamask.auth()
    bot.exchange.withdraw('USDT', 100)
    bot.browser.close_browser()


