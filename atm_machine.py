#!/usr/bin/env python3 
import random

class ATMMachine(object):
    """
    This class is an ATM simulator
    """
    def __init__(self):
        self.accounts = []

    def make_a_withdraw(self, account_number, amount):
        """Withdraw (amount) from (account_number)"""
        "Tengo que identificar la cuenta de la que quiero sacar guita"
        num_cuentas = [i.account_number for i in self.accounts] 
        try: 
          indice = num_cuentas.index(account_number)
          cuenta = self.accounts[indice]
          cuenta.withdraw(amount) 
        except ValueError:
          print 'No existe la Cuenta'
          return
        
    def make_a_deposit(self, account_number, amount):
        """Deposit (amount) into (account_number)"""
        num_cuentas = [i.account_number for i in self.accounts]
        try: 
          indice = num_cuentas.index(account_number)
          cuenta = self.accounts[indice]
          cuenta.deposit(amount)
        except ValueError:
          print 'No existe la Cuenta'
          return

    def print_account_balance(self, account_number):
        """Print the Account Balance from (account_number)"""
        num_cuentas = [i.account_number for i in self.accounts] 
        try:
          indice = num_cuentas.index(account_number)
          cuenta = self.accounts[indice]
          print cuenta.check_balance() 
        except ValueError:
          print 'No existe la Cuenta'
          return    
    
    def make_a_transfer(self, from_account_number, to_account_number, amount):
        """Transfer (amount) from (from_account_number) to (to_account_number)"""
        num_cuentas = [i.account_number for i in self.accounts] 
        try:
          indice_salida = num_cuentas.index(from_account_number)
          cuenta_salida = self.accounts[indice_salida]
          indice_llegada = num_cuentas.index(to_account_number)
          cuenta_llegada = self.accounts[indice_llegada]
          cuenta_salida.transfer_money(amount, cuenta_llegada)
        except ValueError:
          print 'No existe la Cuenta'
          return    
          
    def create_new_account(self, account_number, clients_name, initial_balance):
        """Create a new account that belongs to (clients_name) and has the (initial_balance)"""
        new_account = Account(account_number, clients_name, initial_balance)
        self.accounts.append(new_account)
        
class Account(object):
    """This class represents a simple Account"""
    def __init__(self, account_number, clients_name, initial_balance = 0.0):
        self.account_number = account_number
        self.clients_name = clients_name
        self.balance = initial_balance

    def withdraw(self, amount):
        """Withdraw some money!"""
        if self.balance < amount:
           print 'No tiene fondos suficientes'
        else:
           self.balance -= amount
           
    def deposit(self, amount):
        """Let's receive some money!"""
        self.balance += amount
    
    def check_balance(self):
        """Let's see how rich we are!"""
        return self.balance

    def transfer_money(self, amount, another_account):
        """Transfer money from this account to the other one"""
        if self.balance < amount:
           print 'No tiene fondos suficientes'
        else:
           self.balance -= amount
           another_account.balance += amount


def main():
    atm = ATMMachine()

    """This is the menu"""
    menu_text = """
    1 - Create new Account
    2 - Make a deposit
    3 - Withdraw money
    4 - Check your balance
    5 - Transfer money
    0 - Exit
    """
    while True:
        print("Welcome to the ATM machine")
        print("Choose one of the following options:")
        print(menu_text)
        selected_option = int(input("Option: "))
        print()
        
        if selected_option == 1:
            print("Register new Account:")
            account_number = int(input("Number: "))
            clients_name = input("Name: ")
            initial_balance = float(input("Initial Balance: "))
            atm.create_new_account(account_number, clients_name, initial_balance)

        elif selected_option == 2:
            print("Make a deposit:")
            print("Ingrese el numero de cuenta: ")
            numero_de_cuenta = int(input("Numero de Cuenta: "))
            print("Ingrese el importe a depositar")
            importe = int(input("Importe: "))
            ATMMachine.make_a_deposit(atm,numero_de_cuenta,importe)
            

        elif selected_option == 3:
            print("Withdraw money:")
            print("Ingrese el numero de cuenta: ")
            numero_de_cuenta = int(input("Numero de Cuenta: "))
            ATMMachine.make_a_withdraw(atm, numero_de_cuenta)

        elif selected_option == 4:
            print("Check your balance:")
            print("Ingrese el numero de cuenta: ")
            numero_de_cuenta = int(input("Numero de Cuenta: "))
            ATMMachine.print_account_balance(atm, numero_de_cuenta)

        elif selected_option == 5:
            print("Transfer money:")
            print("Ingrese el numero de cuenta desde donde desea transferir platita: ")
            numero_de_cuenta_inicial = int(input("Numero de Cuenta Inicial: "))
            print("Ingrese el numero de cuenta hacia donde desea transferir platita: ")
            numero_de_cuenta_final = int(input("Numero de Cuenta Final: "))
            print("Ingrese el importe a transferir")
            importe = int(input("Importe: "))
            ATMMachine.make_a_transfer(atm,numero_de_cuenta_inicial,numero_de_cuenta_final,importe)

        elif selected_option == 0:
            print("Bye Bye!")
            exit(0)
        else:
            print("Invalid option!")
        
        print()


if __name__ == '__main__':
    main()
