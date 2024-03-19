class BankAccount:
    def __init__(self,user_name : str, pass_word : str, balance : float) -> None:
        self.username = user_name
        self.password = pass_word
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

#Task 1 Loop over N times and create N objects put it in a list
        
import getpass
total_accounts = []
n=int(input('Enter how many users to create: '))
for i in range(n):
    user_name = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    balance = float(input('Enter bank balance: '))
    total_accounts.append(BankAccount(user_name, password,balance))


# print(total_accounts)
#Task 2 Take username and password from user and check which object it belong to
#task 3 display all information of that user
    
find_username = input('Enter the username to search: ')
find_password = getpass.getpass('Enter password to search: ')
found = False
for object in total_accounts:
    if find_username == object.username and find_password == object.password:
        found = True
        print(f'Object Found') 
        print('Displaying all the information of the searched object: ')
        print(object.username)
        print(object.password)
        print(object.balance)
        break
if not found:
    print('Not Found')


#Task 4 take username of person who you want to send money
#Task 5 find the object  with that username and deposit  the required amount
#Task 6 withdraw amount from your object  and deposit it to target object
receiver_username = input('Enter the username of the person who you want to send money: ')
amount = float(input('Enter the amount to deposit: '))
sender_username = input(f'Enter the username of the person from whom you want to send money to {receiver_username}: ')
receiver_found = False
sender_found = False
for account in total_accounts:
    if receiver_username == account.username:
        receiver_found = True
        account.deposit(amount)
        print(f'Amount deposited to receiver: {amount}')
        print(f'Receiver Balance: {account.balance}')
    if sender_username == account.username:
        sender_found = True
        if account.balance >= amount:
            account.withdraw(amount)
            print(f'Amount withdrawn from sender: {amount}')
            print(f'Sender Balance: {account.balance}')
        else:
            print('Insufficient balance to perform the transaction.')
if not receiver_found:
    print('Receiver not found.')
if not sender_found:
    print('Sender not found.')