class User:
    def __init__(self, driver: bool, occupation, name, email, age, password):
        self.__occupation = occupation
        self.__name = name
        self.__email = email
        self.__age = age
        self.__vehicle = list()
        self.__driver = driver
        self.password = password
        self.boleias = list()

    @property
    def occupation(self):
        return self.__occupation

    @property
    def nome(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def age(self):
        return self.__age

    def store_car(self, car):
        self.__vehicle.append(car)

    @property
    def driver(self):
        return self.__driver

    @property
    def vehicles(self):
        return self.__vehicle

    def is_register(self, vehicle):
        return vehicle in self.vehicles

    def __eq__(self, other):
        return self.email == other.email

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.age}\nEmail: {self.email}\nOcupação: {self.occupation}\n'




