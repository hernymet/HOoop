# Object oriented project hands on 

## ATM machine simulator
The main goal of this hands on session is to build an atm machine simulator. You should download the
[atm_simulator.py](atm_machine.py) module into your home dir. 

The project counts with a single file, a **python3** module that holds the classes for the
`ATMMachine` itself and the `Account` class.


## Assignments

1. Fill the missing methods:
In this assignment you should fill the missing methods and check if the ATM machine is functioning
correctly.
## Hecho

2. Design a solution for generating the `Account` number. Check-out the `random()` operation. Is
that a good way to generate accounts numbers? Can you guarantee that no number appears twice?
    * Think of alternative ways to store the latest account number and derive the next one from it.

3. For each operation you have to go through (possibly) the whole list of accounts in order to
retrieve the account which number has been passed as a parameter. Do you really need to do this?
Think about the data structures presented in previous classes. Is there a better way to perform this
search?


4. Create the following sub-classes:
In this assignment you have to create two specializations for the `Account` class (the corresponding
operations should be rewritten):
    * `CheckingAccount`: This class has the following restrictions:
        * Only 4 free transfers. There is a fee value of 5.0 for each transfer after the 4th.
        * Only 5 free balance checking operation. There is a fee value of 1.00 after the 5th balance 
        checking operation.
    * `SavingsAccount`: This class has the following restrictions:
        * Only 3 free withdrawals. There is a fee value of 2.00 for each withdrawal after the 3rd. 
        * No free transfer. Each transfer has a fee value of 1.00.

5. Check if the account balance allows the requested operation (insufficient funds). If it is not
the case, the user should be warned of his/her current situation.

6. Enhance your balance checking structure by adding Exceptions, in case the client has not enough
funds to perform the requested operation. Exceptions in Python are sub-classes of the basic
exception class `Exception`:

    ```python
    class NotEnoughFundsException(Exception):
        def __init__(self, message):
            self.value = message        
    ```
    
    In order to signal the exceptional behaviour use the `raise` command:
    
    ```python
    if balance <= amount:
        raise NotEnoughFundsException("Check your Balance before")
    ```
    
    In order to deal with the exceptional behaviour use the `try: .. except .. ` construction:
    
    ```python
    try:
        account.withdraw(amount)
    except NotEnoughFundsException:
        print("Dear client, you should check your balance 
            before performing this operation")
    ```
    
    **Question:** Which class do you think should be responsible for raising the exception and which
    should be responsible for dealing with it?

7. Implement a new exception in case an operation resulted in a fee. Present a message for the
client if that is the case.

8. Implement the bank statement functionality. Each operation should be logged at an special list of
Transaction objects (create the `Transaction` class). For each transaction you shoud log the type of
transaction, the date and also the amount involved. Update the menu and the ATMMachine class to
support this new operation.
