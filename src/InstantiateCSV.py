
class InstantiateCSVError(FileNotFoundError):
    """Класс-исключение для проверки корректности файла items.csv"""

    def __str__(self):
        return f"Файл item.csv поврежден"

