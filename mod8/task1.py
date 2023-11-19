class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number
    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if all(isinstance(i, int) for i in coordinates):
            self._coordinates = coordinates
        else:
            raise ValueError('Координаты должны быть целыми числами')

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if (isinstance(speed,int) or isinstance(speed,float)) and speed >= 0:
            self._speed = speed
        else:
            raise ValueError('Скорость должна быть целым числом, не менее нуля')

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError('Бренд должен быть строкой')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if isinstance(year,int):
            self._year = year
        else:
            raise ValueError('Год должен быть целым числом')

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if all(i.isalpha() or i.isdigit() for i in number):
            self._number = number
        else:
            raise ValueError('В номере не должно быть лишних символов, допустимы только буквы и цифры')

    def __str__(self):
        return f"Транспорт: {self._brand} {self._year}, Номер: {self._number}, Текущая скорость: {self._speed}, Координаты: {self._coordinates}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        # Получаем координаты транспорта
        tran_x, tran_y = self.coordinates

        # Проверяем, находится ли транспорт внутри заданной области
        if pos_x <= tran_x <= pos_x + length and pos_y <= tran_y <= pos_y + width:
            return True
        else:
            return False


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int) and passengers_capacity>=0:
            self._passengers_capacity = passengers_capacity
        else:
            raise ValueError('Вместимость должна быть целым числом, не менее нуля')

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and number_of_passengers>=0:
            self._number_of_passengers = number_of_passengers
        else:
            raise ValueError('Текущее количество пассажиров должно быть целым числом, не менее нуля')


class Cargo:
    def __init__(self, carrying):
        self.carrying = carrying

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        # вызов конструктора родительского класса Transport с помощью super()
        super().__init__(coordinates, speed, brand, year, number)
        # устанавливаем уникальный атрибут для класса Plane
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height > 0:
            self._height = height
        else:
            self._height = 0

class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        # вызов конструктора родительского класса Transport с помощью super()
        super().__init__(coordinates, speed, brand, year, number)
        # устанавливаем уникальный атрибут для класса Plane
        
class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, name, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.name = name
        self.port = port

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name,str):
            self._name = name
        else:
            raise ValueError
    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

#----------------------------------------------------------------------------------------------------------------
# следующие классы наследуют от класса Auto

class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number, car_type):
        super().__init__(coordinates, speed, brand, year, number)
        self.car_type = car_type  # тип автомобиля (например, седан, кроссовер, купе)

class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers, bus_type):
        super().__init__(coordinates, speed, brand, year, number)
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers
        self.bus_type = bus_type  # тип автобуса (например, городской, междугородний, туристический)

class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying, cargo_type):
        super().__init__(coordinates, speed, brand, year, number)
        self.carrying = carrying
        self.cargo_type = cargo_type  # тип грузовика (например, фургон, пикап)

#----------------------------------------------------------------------------------------------------------------
# следующие классы наследуют от класса Ship

class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, name, port, boat_type):
        super().__init__(coordinates, speed, brand, year, number, name, port)
        self.boat_type = boat_type  # тип судна (например, яхта, лодка, катер)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, name, port, passengers_capacity, number_of_passengers):
        super().__init__(coordinates, speed, brand, year, number, name, port)
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, name, port, carrying):
        super().__init__(coordinates, speed, brand, year, number, name, port)
        self.carrying = carrying

#----------------------------------------------------------------------------------------------------------------
#следующие классы наследуют от класса Plane

class Aircraft(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height, aircraft_type):
        super().__init__(coordinates, speed, brand, year, number, height)
        self.aircraft_type = aircraft_type

class PassengerAircraft(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers, flight_type):
        super().__init__(coordinates, speed, brand, year, number, height)
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers
        self.flight_type = flight_type
        
    @property
    def flight_type(self,flight_type):
        return flight_type
        
    @flight_type.setter
    def flight_type(self,flight_type):
        if flight_type in ('международный', 'региональный', 'местный'):
            self._flight_type = flight_type #тип перевозок самолёта: международный, региональный или местный
        else:
            raise ValueError('Допустимые типы перевозок: международный, междугородний, местный')


class CargoAircraft(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, carrying, cargoAircraft_type):
        super().__init__(coordinates, speed, brand, year, number, height)
        self.carrying = carrying
        self.cargoAircraft_type = cargoAircraft_type #тип транспортного самолёта, например, военно-транспортный
        
        
# я 2 часа делал только этот класс :)
class Seaplane(Ship, Plane):
    def __init__(self, coordinates, speed, brand, year, number, height, name, port):
        super(Plane, self).__init__(coordinates, speed, brand, year, number)
        self.height = height
        self.name = name
        self.port = port

cargo_auto_instance = CargoAuto(
    coordinates=(111, 200),  # координаты
    speed=100,  # скорость
    brand="Ford",  # марка
    year=2023,  # год выпуска
    number="ABC123",  # номер
    carrying=5000,  # грузоподъемность
    cargo_type="Фургон"  # тип грузовика
)
PassengerAircraft_instance = PassengerAircraft(
    coordinates=(1,3), # координаты
    speed=100, #скорость
    brand='Boeing', #марка
    year=2015, # год выпуска
    number='GK205', # номер
    height=1000, # высота
    passengers_capacity=250, # вместимость пассажиров
    number_of_passengers=170, # текущее количество пассажиров
    flight_type='международный' # тип перевозок
)
seaplane_instance = Seaplane(
    coordinates=(3, 4),  # координаты
    speed=300,  # скорость
    brand="Airbus",  # марка
    year=2022,  # год выпуска
    number="SP123",  # номер
    height=134,  # высота
    name = 'SeaAir', # название модели
    port = 'London Port' # порт
)

print(seaplane_instance)
print(seaplane_instance.__class__.__mro__)
print(PassengerAircraft_instance.__class__.__mro__)
