def deposit(balance , amount):
    balance=balance+amount
    return balance


def withdraw(balance , amount):
    balance=balance-amount
    return balance 



if __name__=="__main__":
    print("---bank---")
    name = input("enter name :")
    initial_balance=float(input("enter balance of your account :"))
    deposited = float(input("enter amount to deposit "))
    balance = deposit (initial_balance, deposited)
    withdrawal= float(input("enter amount to withdraw :"))
    balance = withdraw(initial_balance,withdrawal)
print("name:",name)
print("final balance:",balance)