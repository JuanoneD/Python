# import math
# class Calculator():
#     def __inti__(Self):
#         pass

#     def sum(self):
#         try:
#             num1 = int(input("escreva o primeiro valor"))
#             num2 = int(input("escreva o segundo valor valor"))
#             return num2 + num1
#         except ValueError:
#             return "valor invalido"
    
#     def subtraction(self):
#         try:
#             num1 = int(input("escreva o primeiro valor"))
#             num2 = int(input("escreva o segundo valor valor"))
#             return num1 - num2
#         except ValueError:
#             return "valor invalido"

#     def division(self):
#         try:
#             num1 = int(input("escreva o primeiro valor"))
#             num2 = int(input("escreva o segundo valor valor"))
#             return num1 / num2
#         except ZeroDivisionError:
#             return "numero não pode ser divido por 0"
        
#     def multiplication(self):
#         try:
#             num1 = int(input("escreva o primeiro valor"))
#             num2 = int(input("escreva o segundo valor valor"))
#             return num1 * num2
#         except ValueError:
#             return "valor invalido"

# class ScientificCalculator(Calculator):
#     def __init__(self):
#         pass
#     def power(self):
#         try:
#             num1 = int(input("escreva o primeiro valor"))
#             num2 = int(input("escreva o segundo valor valor"))
#             return num1**num2
#         except ValueError:
#             return "valor invalido"
#     def root(self):
#         try:
#             num1 = int(input("escreva o primeiro valor"))
#             return math.sqrt(num1)
#         except ValueError:
#             return "valor invalido"

# ### main:
# while 1:
#     try:
#         calc = ScientificCalculator()
#         menu = int(input("Escreva: \n 1 == Soma \n 2 == Subtração \n 3 == Multiplicação \n 4 == Divisão \n 5 == Potencia \n 6 == Raiz quadrada \n 0 == Sair"))
#         if menu == 1:
#             print(calc.sum())
#         elif menu == 2:
#            print( calc.subtraction())
#         elif menu == 3:
#             print(calc.multiplication())
#         elif menu == 4:
#             print(calc.division())
#         elif menu == 0:
#             break
#         elif menu == 5:
#             print(calc.power())
#         elif menu == 6:
#             print(calc.root())
#         else:
#             print("valor invalido")
#     except ValueError:
#         print("valor invalido")

class account:
    def __init__(self,name,agency,balance):
        self.__name = name
        self.__agency= agency
        self.__balance = balance

    def Transfer(self,value):
        if value < self.__balance:
            self.__balance -= value
            return "seu novo saldo é " + str(self.__balance)
        else:
            return "saldo insuficiente"
    def Recive(self,value):
        self.__balance += value
        return "seu novo saldo é " + str(self.__balance)
    
    def AccountInfo(self):
        return "Nome: " + str(self.__name) + "\nAgencia: " + str(self.__agency) + "\nSaldo: "+ str(self.__balance)
