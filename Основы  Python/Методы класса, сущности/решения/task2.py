"""
## Задача 2 - medium

1. Создайте класс Metamask, который имеет атрибуты:
- адрес кошелька
- пароль кошелька
- сид фраза
2. Создайте методы, которые имитируют реальное поведение Metamask:
- init для инициализации атрибутов, все 3 атрибуты не обязательны
- auth для авторизации пользователя, при запуске печатает "Вы успешно авторизовались с помощью пароля: {пароль}",
  пароль должен браться из атрибута, при этом если пароль не указан, то печатает "Вы не указали пароль"
- create_wallet для создания кошелька, при запуске генерирует сид фразу из 12 слов, адрес кошелька и пароль
 (если пароль был указан ранее в атрибуте, использует из атрибута, если нет, генерирует случайный пароль), присваивает их
  атрибутам, печатает в терминале "Кошелек успешно создан,   адрес кошелька: {адрес кошелька}, пароль: {пароль}, сид фраза: {сид фраза}"
- import_wallet для импорта кошелька, берет адрес, сид фразу и пароль из атрибутов, если пароль не указан, то генерирует случайный пароль,
  сохраняя его в атрибут, печатает в терминале "Кошелек успешно импортирован, адрес кошелька: {адрес кошелька}, пароль: {пароль}, сид фраза: {сид фраза}"

"""
import random
import string

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'imbe', 'jackfruit',
         'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry',
         'tangerine', 'ugli', 'vanilla', 'watermelon', 'ximenia', 'yellow watermelon', 'zucchini']


class Metamsask:
    def __init__(self, wallet_address: str = None, password: str = None, seed_phrase: str = None):
        """
        Инициализация атрибутов, если атрибуты не указаны, присваивает им значение None
        :param wallet_address: используется для логов, если не указан при создании и импорте кошелька, генерирует случайный адрес
        :param password: используется для авторизации, импорта и создания кошелька, если не указан при создании или импорте кошелька, генерирует случайный пароль
        :param seed_phrase: используется для импорта кошелька, если не указан при создании кошелька, печатает "Сид фраза не указана" и завершает выполнение
        """
        self.wallet_address = wallet_address
        self.password = password
        self.seed_phrase = seed_phrase

    def auth(self) -> None:
        """
        Авторизация пользователя, если пароль не указан печатает "Вы не указали пароль"
        :return: None
        """
        if self.password:
            print(f"Вы успешно авторизовались с помощью пароля: {self.password}")
        else:
            print("Вы не указали пароль")

    def create_wallet(self) -> None:
        """
        Создание кошелька, если пароль не указан, генерирует случайный пароль, если адрес кошелька не указан, генерирует случайный адрес
        :return: None
        """
        if not self.password:
            self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.seed_phrase = ' '.join(random.choices(words, k=12))
        self.wallet_address = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        print(
            f"Кошелек успешно создан, адрес кошелька: {self.wallet_address}, пароль: {self.password}, сид фраза: {self.seed_phrase}")

    def import_wallet(self) -> None:
        """
        Импорт кошелька по сид фразе, если пароль не указан, генерирует случайный пароль, если адрес кошелька не указан, генерирует случайный адрес.
        Если сид фраза не указана, печатает "Сид фраза не указана" и завершает выполнение.
        :return: None
        """
        if not self.seed_phrase:
            print("Сид фраза не указана")
            return
        if not self.password:
            self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if not self.wallet_address:
            self.wallet_address = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        print(
            f"Кошелек успешно импортирован, адрес кошелька: {self.wallet_address}, пароль: {self.password}, сид фраза: {self.seed_phrase}")
