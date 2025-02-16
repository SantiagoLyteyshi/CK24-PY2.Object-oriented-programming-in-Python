from typing import Union, Optional, List
from pydantic import BaseModel, Field


class TransportVehicle(BaseModel):
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        name (str): Название транспортного средства.
        speed (Union[int, float]): Скорость транспортного средства.
        capacity (int): Вместимость транспортного средства.
    """
    name: str
    speed: Union[int, float] = Field(..., gt=0, description="Скорость должна быть положительной")
    capacity: int = Field(..., gt=0, description="Вместимость должна быть положительной")

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        :return: Строковое представление

        Примеры:
        >>> vehicle = TransportVehicle(name="Random Vehicle", speed=100, capacity=5)
        >>> str(vehicle)
        'Random Vehicle (Скорость: 100 км/ч, Вместимость: 5 человек)'
        """
        return f"{self.name} (Скорость: {self.speed} км/ч, Вместимость: {self.capacity} человек)"

    def move(self) -> str:
        """
        Метод для движения транспортного средства.

        :return: Сообщение о движении

        Примеры:
        >>> vehicle = TransportVehicle(name="Random Vehicle", speed=100, capacity=5)
        >>> vehicle.move()
        'Random Vehicle движется со скоростью 100 км/ч.'
        """
        return f"{self.name} движется со скоростью {self.speed} км/ч."


class Ship(TransportVehicle):
    """
    Дочерний класс для кораблей.

    Атрибуты:
        draft (Union[int, float]): Осадка корабля.
    """
    draft: Union[int, float] = Field(..., gt=0, description="Осадка должна быть положительной")

    def move(self) -> str:
        """
        Перегруженный метод для движения корабля.

        :return: Сообщение о движении корабля

        Примеры:
        >>> ship = Ship(name="Titanic", speed=30, capacity=2000, draft=10.5)
        >>> ship.move()
        'Titanic плывет по воде со скоростью 30 км/ч.'
        """
        return f"{self.name} плывет по воде со скоростью {self.speed} км/ч."


class Airplane(TransportVehicle):
    """
    Дочерний класс для самолетов.

    Атрибуты:
        altitude (Union[int, float]): Высота полета.
    """
    altitude: Union[int, float] = Field(..., gt=0, description="Высота должна быть положительной")

    def move(self) -> str:
        """
        Перегруженный метод для движения самолета.

        :return: Сообщение о движении самолета

        Примеры:
        >>> airplane = Airplane(name="Boeing 747", speed=900, capacity=416, altitude=10000)
        >>> airplane.move()
        'Boeing 747 летит на высоте 10000 м со скоростью 900 км/ч.'
        """
        return f"{self.name} летит на высоте {self.altitude} м со скоростью {self.speed} км/ч."


class Car(TransportVehicle):
    """
    Дочерний класс для автомобилей.

    Атрибуты:
        fuel_type (str): Тип топлива.
    """
    fuel_type: str

    def move(self) -> str:
        """
        Перегруженный метод для движения автомобиля.

        :return: Сообщение о движении автомобиля

        Примеры:
        >>> car = Car(name="Toyota Corolla", speed=180, capacity=5, fuel_type="бензин")
        >>> car.move()
        'Toyota Corolla едет по дороге со скоростью 180 км/ч.'
        """
        return f"{self.name} едет по дороге со скоростью {self.speed} км/ч."


class Fleet(BaseModel):
    """
    Класс для управления коллекцией транспортных средств.

    Атрибуты:
        vehicles (Optional[List[TransportVehicle]]): Список транспортных средств.
    """
    vehicles: Optional[List[TransportVehicle]] = []

    def get_next_vehicle_id(self) -> int:
        """
        Возвращает следующий id для нового транспортного средства.

        Возвращает:
            int: Следующий id.
        """
        if not self.vehicles:
            return 1
        return self.vehicles[-1].id + 1

    def get_index_by_vehicle_id(self, vehicle_id: int) -> int:
        """
        Возвращает индекс транспортного средства по его id.

        Аргументы:
            vehicle_id (int): id транспортного средства.

        Возвращает:
            int: Индекс транспортного средства.

        Исключения:
            ValueError: Если транспортное средство с указанным id не найдено.
        """
        for index, vehicle in enumerate(self.vehicles):
            if vehicle.id == vehicle_id:
                return index
        raise ValueError("Транспортное средство с запрашиваемым id не существует")
