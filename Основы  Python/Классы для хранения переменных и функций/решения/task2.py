"""
Создайте класс Config (не подсматривайте в уроке), в котором будут храниться данные:
- список номеров профилей
- пауза между запуском профилей
- настройка для включения/выключения использования прокси
- ссылка на url метамаска в профиле
"""
class Config:
    """
    Класс для хранения настроек

    Аргументы:

    - profile_numbers (list) - список номеров профилей
    - pause_between_profiles (int) - пауза между профилями
    - use_proxy (bool) - использование прокси

    """

    profile_numbers: list = [1, 2, 3]
    pause_between_profiles: int = 10
    use_proxy: bool = True
    metamask_url: str = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"
