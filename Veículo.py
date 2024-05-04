class Boleia:
    def __init__(self, origin: str, destiny: str, date, hour: str):
        self.origin = origin
        self.destiny = destiny
        self.date = date
        self.hour = hour
        self.__status = 'Available'
        self.__evaluation = 'Not evaluated'

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        self.__status = new_status

    @property
    def evaluation(self):
        return f"{self.__evaluation} estrelas" if self.__evaluation.isnumeric() else self.__evaluation

    @evaluation.setter
    def evaluation(self, new_evaluation):
        self.__evaluation = new_evaluation

    def __str__(self):
        return f"Origem: {self.origin}\nDestino: {self.destiny}\nData: {self.date}\nHour: {self.hour}\nEstado: {self.__status}\nAvaliação: {self.evaluation}"


class Vehicle:
    def __init__(self, color: str, seats: int, brand: str, placa: str):
        self.__brand = brand
        self.__color = color
        self.__seats = seats
        self.__placa = placa
        self.rides = list()

    @property
    def brand(self):
        return self.__brand

    @property
    def color(self):
        return self.__color

    @property
    def seats(self):
        return self.__seats

    @property
    def placa(self):
        return self.__placa

    def __eq__(self, other):
        return self.__placa == other.__placa

    def __str__(self):
        return f"Matrícula: {self.__placa}\nMarca: {self.__brand}\nCor: {self.__color}\nSeats: {self.__seats}\nDados da Viagem:\n"
