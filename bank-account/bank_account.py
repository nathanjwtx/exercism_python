import threading


class BankAccount(object):
    account_open = False
    balance_lock = threading.Lock()

    def __init__(self):
        self.balance = 0

    def get_balance(self):
        if self.account_open:
            with self.balance_lock:
                return self.balance
        else:
            self.closed_exception()

    def open(self):
        if not self.account_open:
            self.account_open = True
        else:
            raise ValueError("Account already open")

    def deposit(self, amount):
        if self.account_open:
            if amount >= 0:
                with self.balance_lock:
                    self.balance += amount
            else:
                raise ValueError("Negative amount")
        else:
            self.closed_exception()

    def withdraw(self, amount):
        if self.account_open:
            with self.balance_lock:
                if 0 <= amount <= self.balance:
                    self.balance -= amount
                elif amount < 0:
                    raise ValueError("Negative amount")
                else:
                    raise ValueError()
        else:
            self.closed_exception()

    def close(self):
        if self.account_open:
            self.balance = 0
            self.account_open = False
        else:
            self.closed_exception()

    def closed_exception(self):
        raise ValueError("Account closed")
