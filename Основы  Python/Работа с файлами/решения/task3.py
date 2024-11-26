from __future__ import annotations

import os


def get_list_from_file(
        name: str,
        is_number: bool = False,
) -> list[str | int]:
    """
    Get list from file
    :param name: название файла с указанием расширения, файл должен находиться в папке config/data
    :param is_number: если True, то возвращаем список чисел
    :return: список строк из файла
    """
    file_path = 'data/' + name

    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}, создали пустой файл")
        with open(file_path, "w") as file:
            file.write("")


    with open(file_path, "r") as file:
        data = file.read().splitlines()
        if is_number:
            return [int(line) for line in data]
        return data
