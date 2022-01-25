import sys


class Account:

    def __init__(self, name: str, opening_balance: float = 0.0):

        self.name = name
        self._balance = opening_balance
        print("Account created for {} ".format(name))
        self.show_balance()

    def deposit(self, amount: float) -> float:

        if amount > 0.0:
            self._balance += amount
            print("Deposit {} pounds".format(amount))
        return self._balance

    def withdraw(self, amount: float) -> float:

        if amount > 0.0:

            if amount <= self._balance:

                self._balance -= amount
                print("Withdraw {} pounds".format(amount))
                return self._balance

            else:

                print("Your balance is less than amount")
                return 0.0

        else:

            print("Enter positive amount")

    def show_balance(self) -> str:

        print("Balance on account {} is {}".format(self.name, round(self._balance, 4)))


def main() -> None:

    client = Account("John")

    while True:

        op = input("Press 1 to deposit or 2 for withdrawal or 0 to quit:")

        if op == '1':

            d = float(input("Deposit :"))

            client.deposit(d)
            client.show_balance()

        if op == '2':

            w = float(input("Withdraw :"))

            client.withdraw(w)
            client.show_balance()

        if op == '0':

            client.show_balance()

            sys.exit()


main()
