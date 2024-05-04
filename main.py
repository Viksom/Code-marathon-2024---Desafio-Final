from Utilizador import *
from Veículo import *


class System:
    def __init__(self):
        self.users = list()
        self.__user = None
        self.menus = [
            ["Criar Conta", "Login", "Sair"],
            ["Encontrar Boleias", "Avaliar Boleias", "Terminar Sessão"],
            ["Adicionar Veículo", "Publicar Boleia", "Terminar Sessão"]
                    ]
        self.options = [
            ["Aluno", "Professor", "Funcionário"],
            ["Utilizador", "Condutor"]
                      ]

    def create_account(self):
        name = input("Nome: ")
        age = input("Idade: ")
        email = input("Email: ")
        password = input("Password: ")
        driver = None
        while driver not in range(1, len(self.options[1]) + 1):
            count1 = 1
            for d in self.options[1]:
                print(f" {count1} -> {d}")
                count1 += 1
            driver = int(input("Opção: "))
        driver = False if driver == 1 else True
        occupation = None
        while occupation not in range(1, len(self.options[0]) + 1):
            count2 = 1
            for o in self.options[0]:
                print(f" {count2} -> {o}")
                count2 += 1
            occupation = int(input("Opção: "))
        user = User(driver, self.options[0][occupation - 1], name, email, age, password)
        if user in self.users:
            return False
        self.users.append(user)
        return True

    def login(self):
        email = input("Email: ")
        password = input("Password: ")
        for user in self.users:
            if user.email == email:
                if password == user.password:
                    self.__user = user
                    return True
        return False

    def add_vehicle(self):
        color = input("Cor do veículo: ")
        seats = int(input("Lugares disponíveis no veículo: "))
        brand = input("Marca do veículo: ")
        placa = input("Matrícula do veículo: ")
        vehicle = Vehicle(color, seats, brand, placa)
        if self.__user.is_register(vehicle):
            return False
        self.__user.vehicles.append(vehicle)
        return True

    def find_ride(self):
        print('Indique as opções da sua boleia')
        origin = input('Origem da Boleia: ')
        destiny = input('Destino da Boleia: ')
        date = input('Data da Boleia: ')
        hour = input('Hora da Boleia: ')
        rides = list()
        for user in self.users:
            if user.driver:
                for vehicle in user.vehicles:
                    for ride in vehicle.rides:
                        if origin == ride.origin and destiny == ride.destiny and date == ride.date == date and hour == ride.hour:
                            rides.append([vehicle, ride])
        option_ride = None
        if len(rides) == 0:
            print("Não há boleias com estas características.")
        else:
            while option_ride not in range(1, len(rides) + 2):
                count = 1
                for ride in rides:
                    print("-=" * 15)
                    print(f"{count} - {ride[0]}\n{ride[1]}")
                    count += 1
                print("-=" * 15)
                print(f"{count} - Não reservar.")
                option_ride = int(input("Selecione uma boleia para reservar: "))
            if option_ride < len(rides) + 1:
                if rides[option_ride - 1][1].status == "Unavailable":
                    print("Esta boleia já foi reservada.")
                else:
                    rides[option_ride - 1][1].status = "Unavailable"
                    self.__user.boleias.append(rides[option_ride - 1])
                    print("Boleia reservada com sucesso.")

    def publish_ride(self):
        if len(self.__user.vehicles) == 0:
            return False
        else:
            option_vehicle = None
            while option_vehicle not in range(1, len(self.__user.vehicles) + 1):
                contador = 1
                for vehicle in self.__user.vehicles:
                    print(f"{contador} - {vehicle.brand} / {vehicle.placa}")
                    contador += 1
                option_vehicle = int(input("> "))
            print('Dados da boleia')
            origin = input('Origem da Boleia: ')
            destiny = input('Destino da Boleia: ')
            date = input('Data da Boleia: ')
            hour = input('Hora da Boleia: ')
            self.__user.vehicles[option_vehicle - 1].rides.append(Boleia(origin, destiny, date, hour))
            return True

    def evaluation(self):
        if len(self.__user.boleias) > 0:
            option_evaluation = None
            while option_evaluation not in range(1, len(self.__user.boleias) + 1):
                count = 1
                for i in self.__user.boleias:
                    print("=-" * 15)
                    print(f"{count} - {i[1]}")
                    count += 1
                option_evaluation = int(input("> "))
            print(f"Selecionou: \n{self.__user.boleias[option_evaluation - 1][1]}")
            aval = None
            while aval not in range(1, 6):
                aval = int(input("Como avalias de 1 a 5: "))
            self.__user.boleias[option_evaluation - 1][1].evaluation = aval
            print("Obrigado pela avaliação!")
        else:
            print("Sem boleias para avaliar.")

    def run(self):
        while True:
            option = None
            while option not in range(1, len(self.menus[0]) + 1):
                count = 1
                for i in self.menus[0]:
                    print(f"{count} - {i}")
                    count += 1
                option = int(input("> "))
            if option == 1:
                if self.create_account():
                    print("Conta criada com sucesso.\n")
                else:
                    print("Este email já foi registado.\n")
            elif option == 2:
                if not self.login():
                    print("Palavra passe ou email incorreto.")
                else:
                    if self.__user.driver:
                        logged = True
                        while logged:
                            option_driver = None
                            while option_driver not in range(1, len(self.menus[2]) + 1):
                                count1 = 1
                                for d in self.menus[2]:
                                    print(f" {count1} -> {d}")
                                    count1 += 1
                                option_driver = int(input("Opção: "))
                            if option_driver == 1:
                                if self.add_vehicle():
                                    print("Veículo adicionado com sucesso!")
                                else:
                                    print("O veículo já foi registado.")
                            elif option_driver == 2:
                                if self.publish_ride():
                                    print("Boleia publica com sucesso.")
                                else:
                                    print("Não existem veículos disponíveis.")
                            else:
                                self.__user = None
                                print('Volte Sempre!')
                                logged = False
                    else:
                        logged = True
                        while logged:
                            count = 1
                            option_user = None
                            while option_user not in range(1, len(self.menus[1]) + 1):
                                for opt in self.menus[1]:
                                    print(f"{count} - {opt}")
                                    count += 1
                                option_user = int(input("> "))
                            if option_user == 1:
                                self.find_ride()
                            elif option_user == 2:
                                self.evaluation()
                            else:
                                self.__user = None
                                print('Volte Sempre!')
                                logged = False
            else:
                return


# Press the green button in the gutter to run the script
if __name__ == '__main__':
    app = System()
    app.run()
    print("Fim do Projecto")
