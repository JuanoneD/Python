class Account:
    def __init__(self,name,agency,balance):
        self._name = name
        self._agency= agency
        self._balance = balance

    def Withdraw(self,value):
        if value < self._balance:
            self._balance -= value
            return "voce sacou " + str(value) + "seu novo saldo é" + str(self._balance)
        else:
            return "saldo insuficiente"
    def Recive(self,value):
        self._balance += value
        return "seu novo saldo é " + str(self._balance)
    
    def AccountInfo(self):
        return "Nome: " + str(self._name) + "\nAgencia: " + str(self._agency) + "\nSaldo: "+ str(self._balance)

class WageAccount(Account):
    def __init__(self,name,agency,balance):
        super().__init__(name,agency,balance)
        pass

class CurrentAccount(Account):
    def __init__(self,name,agency,balance,credit):
        super().__init__(name,agency,balance)
        self.__CreditCard = credit
    def Transfer(self,people,value):
        if value < self._balance:
            self._balance -= value
            return "voce transferiu" + str(value) + "para" + people
        else:
            return "valor insuficiente"
    def Invest(self,place,value):
        if value < self._balance:
            self._balance -= value
            return "voce investiu" + str(value) + "em" + place
    
    def CreditCard(self):
        return "Seu valor de credito é " + str(self.__CreditCard)

class SavingAccount(Account):
    def __init__(self, name, agency, balance):
        super().__init__(name, agency, balance)


    def Transfer(self,people,value):
        if value < self._balance:
            self._balance -= value
            return "voce transferiu" + str(value) + "para" + people
        else:
            return "valor insuficiente"  
## MAIN:
while 1:
    try:
        menu = int(input("Escreva \n1 == Conta Corrente \n2 == Conta Salario \n3 == Conta Poupança \n0 == Sair"))
        match menu:
            case 1:
                name = input("escreva seu nome: ")
                agency = int(input("escreva sua agencia: "))
                value = int(input("escreva seu valor para primeiro deposito"))
                credit = int(input("escreva seu valor de credito"))
                user = CurrentAccount(name,agency,value,credit)
                while 1:
                    try:
                        menu2 = int(input("Escreva \n1 == Sacar \n2 == Depositar \n3 == Dados da conta \n4 == Trasferencia \n5 == Investir \n6 == Saldo de credito \n 0 == sair"))
                        match menu2:
                            case 0:
                                break
                            case 1:
                                value = int(input("Escreva o valor do saque"))
                                print(user.Withdraw(value))
                            case 2:
                                value = int(input("Escreva o valor do Depositar"))
                                print(user.Recive(value))
                            case 3:
                                print(user.AccountInfo())
                            case 4:
                                people = input("escreva a pessoa pra receber a transferencia")
                                value = int(input("escreva o valor da transferencia"))
                                print(user.Transfer(people,value))
                            case 5:
                                place = input("escreva a pessoa pra recever a transferencia")
                                value = int(input("escreva o valor da transferencia"))
                                print(user.Invest(place,value))
                            case 6:
                                print(user.CreditCard)
                            case _:
                                print("valor invalido")
                    except ValueError:
                        print("valor errado")
            case 2:
                name = input("escreva seu nome: ")
                agency = int(input("escreva sua agencia: "))
                value = int(input("escreva seu valor do salario"))
                user = WageAccount(name,agency,value)
                while 1:
                    try:
                        menu2 = int(input("Escreva \n1 == Sacar \n2 == Receber \n3 == Dados da conta \n0 == sair"))
                        match menu2:
                            case 0:
                                break
                            case 1:
                                value = int(input("Escreva o valor do saque"))
                                print(user.Withdraw(value))
                            case 2:
                                value = int(input("Escreva o valor recebido"))
                                print(user.Recive(value))
                            case 3:
                                print(user.AccountInfo())
                            case _:
                                print("valor invalido")
                    except ValueError:
                        print("valor invalido")
        
            case 3:
                name = input("escreva seu nome: ")
                agency = int(input("escreva sua agencia: "))
                value = int(input("escreva seu valor do salario"))
                user = SavingAccount(name,agency,value)
                while 1:
                    try:
                        menu2 = int(input("Escreva \n1 == Sacar \n2 == Depositar \n3 == Dados da conta  \n 0 == sair"))
                        match menu2:
                            case 0:
                                break
                            case 1:
                                value = int(input("Escreva o valor do saque"))
                                print(user.Withdraw(value))
                            case 2:
                                value = int(input("Escreva o valor do Depositar"))
                                print(user.Recive(value))
                            case 3:
                                print(user.AccountInfo())
                            case 4:
                                people = input("escreva a pessoa pra receber a transferencia")
                                value = input ("valor da transferencia")
                                print(user.Transfer(people,value))
                            case _:
                                print("valor invalido")
                    except ValueError:
                        print("valor invalido")

            case 0:
                break
            case _:
                print("valor invalido")
            
    except ValueError:
        print("valor invalido")




        