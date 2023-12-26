import os
import sys
from abc import ABC, abstractmethod

PREFIX = "TitaniumShop"
SYSTEM_CLEAR = "cls"


class PeripheralDevice(ABC):
    def __init__(self, serial_number, brand, price):
        self.serial_number = serial_number
        self.brand = brand
        self.price = price

    @abstractmethod
    def get_info(self):
        pass


class Headphones(PeripheralDevice):
    def __init__(self, serial_number, brand, price, construction_type, mounting_method):
        super().__init__(serial_number, brand, price)
        self.construction_type = construction_type
        self.mounting_method = mounting_method

    def get_info(self):
        return f"Наушники - серийный номер: {self.serial_number}, Бренд: {self.brand}, Цена: {self.price}, " \
               f"Типа конструкции: {self.construction_type}, Метод крепления: {self.mounting_method}"


class Microphone(PeripheralDevice):
    def __init__(self, serial_number, brand, price, frequency_range, sensitivity):
        super().__init__(serial_number, brand, price)
        self.frequency_range = frequency_range
        self.sensitivity = sensitivity

    def get_info(self):
        return f"Микрофон - серийный номер: {self.serial_number}, Бренд: {self.brand}, Цена: {self.price}, " \
               f"Частотный диапазон: {self.frequency_range}, Чувствительность: {self.sensitivity}"


class Keyboard(PeripheralDevice):
    def __init__(self, serial_number, brand, price, switch_type, interface):
        super().__init__(serial_number, brand, price)
        self.switch_type = switch_type
        self.interface = interface

    def get_info(self):
        return f"Клавиатура - серийный номер: {self.serial_number}, Бренд: {self.brand}, Цена: {self.price}, " \
               f"Тип выключателя: {self.switch_type}, Интерфейс: {self.interface}"


# Абстрактный класс для фабричных методов создания устройств
class PeripheralDeviceFactory(ABC):
    @abstractmethod
    def create_device(self, **kwargs):
        pass


# Фабричный метод для создания наушников
class HeadphonesFactory(PeripheralDeviceFactory):
    def create_device(self, **kwargs):
        return Headphones(**kwargs)


# Фабричный метод для создания микрофонов
class MicrophoneFactory(PeripheralDeviceFactory):
    def create_device(self, **kwargs):
        return Microphone(**kwargs)


# Фабричный метод для создания клавиатур
class KeyboardFactory(PeripheralDeviceFactory):
    def create_device(self, **kwargs):
        return Keyboard(**kwargs)


# Функция для добавления устройства
def add_device(devices):
    print("\nВыберите тип девайса:")
    print("1. Наушники")
    print("2. Микрофон")
    print("3. Клавиатура")

    choice = input("\nВыберите необходимое действие (введите соответствующую цифру) >> ")

    if choice not in ["1", "2", "3"]:
        print(f"\n[{PREFIX}] Неверный выбор. Пожалуйста, попробуйте снова.")
        return

    serial_number = input("Введите серийный номер: ")

    # Проверка на уникальность серийника
    for device in devices:
        if device.serial_number == serial_number:
            print(f"\n[{PREFIX}] Устройство с таким серийным номером уже существует!")
            return

    brand = input("Введите бренд: ")
    price = float(input("Введите цену: "))

    if choice == "1":
        construction_type = input("Введте тип конструкции: ")
        mounting_method = input("Введите способ крепления: ")
        factory = HeadphonesFactory()
        device = factory.create_device(
            serial_number=serial_number, brand=brand, price=price,
            construction_type=construction_type, mounting_method=mounting_method
        )
    elif choice == "2":
        frequency_range = input("Введите диапазон частот: ")
        sensitivity = input("Введите чувствительность: ")
        factory = MicrophoneFactory()
        device = factory.create_device(
            serial_number=serial_number, brand=brand, price=price,
            frequency_range=frequency_range, sensitivity=sensitivity
        )
    elif choice == "3":
        switch_type = input("Введите тип выключателя: ")
        interface = input("Введите интерфейс: ")
        factory = KeyboardFactory()
        device = factory.create_device(
            serial_number=serial_number, brand=brand, price=price,
            switch_type=switch_type, interface=interface
        )
    else:
        print(f"[{PREFIX}] Неверный выбор. Пожалуйста, введите число от 1 до 3.")
        return

    devices.append(device)
    print(f"\n[{PREFIX}] Устройство успешно добавлено:")
    print(device.get_info())


def rem_device(devices):
    serial_number = input("Введите серийный номер: ")

    for device in devices:
        if device.serial_number == serial_number:
            print(f"\n[{PREFIX}] Устройство успешно удалено:")
            print(device.get_info())
            devices.remove(device)  # Удаление устройства из списка
            return

    print(f"\n[{PREFIX}] Девайс с таким серийным номером {serial_number} не найден.")


def display_devices(devices):
    print(f"\nЛист девайсов:")
    for device in devices:
        print(device.get_info())


def display_device_by_serial_number(devices, serial_number):
    for device in devices:
        if device.serial_number == serial_number:
            print("\nИнформация о девайсе:")
            print(device.get_info())
            return
    print(f"[{PREFIX}] Девайс с таким серийным номером {serial_number} не найден.")


def show_menu():
    print("\n============ " + PREFIX + " ============")
    print("1. Добавить новый девайс")
    print("2. Вывести весь список девайсов")
    print("3. Вывести устройство по серийному номеру")
    print("4. Удалить устройство")
    print("5. Выход из программы")
    print("=======================================")


if __name__ == "__main__":
    devices_list = []

    while True:
        show_menu()  # Выводим меню на экран
        user_choice = input("\nВыберите необходимое действие (введите соответствующую цифру) >> ")

        match user_choice:
            case "1":
                add_device(devices_list)
                continue

            case "2":
                display_devices(devices_list)
                continue

            case "3":
                serial_number = input("Введите серийный номер: ")
                display_device_by_serial_number(devices_list, serial_number)
                continue

            case "4":
                rem_device(devices_list)
                continue

            case "5":
                sys.exit()

            case _:
                print("[" + PREFIX + "] Ошибка: Неверный выбор. Пожалуйста, введите число от 1 до 6.")
