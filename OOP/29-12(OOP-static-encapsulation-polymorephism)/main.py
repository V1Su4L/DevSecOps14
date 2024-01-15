class BankAccount:
    def __init__(self, name, password, account_id, balance):
        self.name = name
        self.password = password
        self.account_id = account_id
        self.__balance = balance  # private member
        self._credit_score = 5  # protected member

    def get_balance(self):
        return self.__balance * 0.9

    def set_balance(self, new_value):
        if new_value > 0:
            self.__balance = new_value


acc1 = BankAccount('hodi', 1234, 205011, 190)

# print(acc1)
# print(acc1.balance)
# print(acc1.get_balance())
print(acc1._credit_score)
print(acc1.get_balance())
acc1.set_balance(20000)
# acc1.__balance = 50 #X
print(acc1.get_balance())
# print(acc1.__balance)  # -> __balance = 50 it's not the balance attribute its __balance
