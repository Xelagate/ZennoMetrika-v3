def get_wallets(file_path: str = "data/wallets.txt") -> list[str]:
    """
    Функция возвращает список кошельков из текстового файла.
    :param file_path: путь к файлу, по умолчанию равен "data/wallets.txt"
    :return: список кошельков
    """
    with open(file_path, "r") as file:
        wallets = file.read().splitlines()
    return wallets
