class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds!")
      return 0
    else:
      self.balance -= amount
      return amount

  def display_balance(self):
    print("Hi " + f"{self.first_name} {self.last_name}!" +  " Your Current balance: $" + str(self.balance))

account = BankAccount('Lucas', 'Melo', 1, 'Cheking', 1234, 100)

account.deposit(96)
account.withdraw(25)
account.display_balance()
