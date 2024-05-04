from main import System
from Veículo import *

app = System()


def test_login():
    if app.add_vehicle():
        print("Veículo adicionado.")
    else:
        print("Veículo não adicionado!")

def test_vehicle_comparation():
    v1 = Vehicle("White", 4, "Smart", "23ab12")
    v2 = Vehicle("Blue", 4, "Ferrari", "23ab12")
    if v1 == v2:
        print("Os veículos são iguais")
    else:
        print("Os veiculos são diferentes.")
