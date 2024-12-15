import doctest
import math
from typing import Union

# TODO Написать 3 класса с документацией и аннотацией типов
class Dvigatel:
    def __init__(self, krytyashiy_moment: Union[int, float], chastota_oborotov: Union[int, float]) -> None:
        if not isinstance(krytyashiy_moment, (int, float)):
            raise TypeError
        if krytyashiy_moment < 0:
            raise ValueError
        self.krytyashiy_moment = krytyashiy_moment

        if not isinstance(chastota_oborotov, (int, float)):
            raise TypeError
        if chastota_oborotov < 0:
            raise ValueError
        self.chastota_oborotov = chastota_oborotov
        """
            Создание и подготовка к работе объекта "Двигатель"

            :param krytyashiy_moment: Крутящий момент двигателя
            :param chastota_oborotov: Частота оборотов двигателя

            :raise ValueError: Если крутящий момент или частота оборотов двигателя меньше нуля или равны нулю, то вызываем
            
            Примеры:
            >>> dvigatel = Dvigatel(148, 4200)  # инициализация экземпляра класса
            """

    def raschet_moshnosti_v_ls(self):
        """
            Функция, которая считает мощность двигателя в лошадиных силах

            Примеры:
            >>> dvigatel = Dvigatel(148, 4200) # инициализация экземпляра класса
            >>> dvigatel.raschet_moshnosti_v_ls() # расчет мощности двигателя
            """
        self.moshnost = self.krytyashiy_moment * self.chastota_oborotov / 7025

    def raschet_moshnosti_v_kwt(self) -> None:
        """
            Функция, которая считает мощность двигателя в киловаттах

            Примеры:
            >>> dvigatel = Dvigatel(148, 4200) # инициализация экземпляра класса
            >>> dvigatel.raschet_moshnosti_v_kwt() # расчет мощности двигателя
            """
        self.moshnost = self.krytyashiy_moment * self.chastota_oborotov / 9550

class Zagotovka:
    def __init__(self, diameter: Union[int, float], length: Union[int, float]) -> None:
        """
            Создание и подготовка к работе объекта "Заготовка"

            :param diameter: Диаметр заготовки
            :param length: Длина заготовки

            :raise ValueError: Если диаметр или длина меньше нуля или равны нулю, то вызываем

            Примеры:
            >>> zagotovka = Zagotovka(100, 200)  # инициализация экземпляра класса
            """
        if not isinstance(diameter, (int, float)):
            raise TypeError
        if diameter <= 0:
            raise ValueError
        self.diameter = diameter
        if not isinstance(length, (int, float)):
            raise TypeError
        if length <= 0:
            raise ValueError
        self.length = length

    def objem(self) -> None:
        """
            Функция, которая считает объем заготовки

            Примеры:
            >>> zagotovka = Zagotovka(100, 200) # инициализация экземпляра класса
            >>> zagotovka.objem() # расчет объема заготовки
            """
        self.objem = math.pi * self.diameter**2 * self.length

    def protochit(self, pripusk: Union[int, float], dlina: Union[int, float]) -> None:
        """
            Точение заготовки.
            :param pripusk: Припуск на диаметр
            :param dlina: Припуск на торцы

            :raise ValueError: Если припуск на диаметр или на торцы меньше нуля, то вызываем

            Примеры:
            >>> zagotovka = Zagotovka(100, 200)  # инициализация экземпляра класса
            >>> zagotovka.protochit(4,6) # удалить материал
            """
        if not isinstance(pripusk, (int, float)):
            raise TypeError
        if pripusk < 0:
            raise ValueError
        self.diameter -= pripusk
        if not isinstance(dlina, (int, float)):
            raise TypeError
        if dlina < 0:
            raise ValueError
        self.length -= dlina

class Shcola:
    def __init__(self, nachalo_yrokov: int, vremya_bydilnika: int) -> None:
        """
            Создание и подготовка к работе объекта "Школа"

            :param nachalo_yrokov: Время начала уроков
            :param vremya_bydilnika: Время звонка будильника

            :raise ValueError: Если время начала уроков или звонка будильника меньше нуля или равны нулю, то вызываем

            Примеры:
            >>> shcola = Shcola(30, 5) # инициализация экземпляра класса
            """
        if not isinstance(nachalo_yrokov, int):
            raise TypeError
        if nachalo_yrokov < 0:
            raise ValueError
        self.nachalo_yrokov = nachalo_yrokov
        if not isinstance(vremya_bydilnika, int):
            raise TypeError
        if vremya_bydilnika < 0:
            raise ValueError
        self.vremya_bydilnika = vremya_bydilnika

    def perevesti_bydilnik(self, time: int) -> None:
        """
            Перевести будильник.
            :param time: Время, на которое переводим будильник

            :raise ValueError: Если время меньше нуля, то вызываем

            Примеры:
            >>> shcola = Shcola(30, 5) # инициализация экземпляра класса
            >>> shcola.perevesti_bydilnik(10) # перевести будильник
            """
        if not isinstance(time, int):
            raise TypeError
        if time < 0:
            raise ValueError
        self.vremya_bydilnika += time

    def opozdanie(self) -> bool:
        """
            Функция которая проверяет, опоздаю ли я в школу

            :return: Опоздаю ли я в школу

            Примеры:
            >>> shcola = Shcola(30, 5) # инициализация экземпляра класса
            >>> shcola.opozdanie() # проверка опоздания
            """
        return self.nachalo_yrokov - self.vremya_bydilnika <= 0

# if __name__ == "__main__":
#     # TODO работоспособность экземпляров класса проверить с помощью doctest
#     doctest.testmod()  # тестирование примеров, которые находятся в документаци
#     pass
