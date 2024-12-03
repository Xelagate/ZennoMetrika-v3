
class Account:
    """
    Класс для хранения данных об аккаунте

    Аргументы:

    - profile_number (int) - номер профиля
    - wallet_address (str) - адрес кошелька
    - password (str) - пароль
    - private_key (str) - приватный ключ
    - seed (str) - сид фраза

    """

    profile_number: int = 949
    wallet_address: str = '0x1234567890'
    password: str = 'qwerty'
    private_key: str = '1234567890'
    seed: str

    @staticmethod
    def generate_password() -> str:
        """
        Генерация случайной строки из 8 символов
        :return: сгенерированный пароль
        """
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
