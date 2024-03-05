class House:
    def __init__(self,area,rua,cor,nome="Alguem"):
        self.area = area
        self.rua = rua
        self.cor = cor
        self.nome = nome

    def print_house(self):
        print(f"Area {self.area} rua {self.rua} da casa {self.cor} de {self.nome}")

house_jao = House("240","terra roxa","azul","carlos")
house_jao.print_house()
