class Bank_account:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


data_list = input().split(" | ")

acc_list = []
while not data_list[0] == "end":
    bank = data_list[0]
    name = data_list[1]
    balance = float(data_list[2])

    bank_account = Bank_account(name = name, bank = bank, balance = balance)
    acc_list.append(bank_account)

    data_list = input().split(" | ")

for account in sorted(acc_list, key = lambda acc: (-acc.balance, len(acc.bank)) ):
    print(f"{account.name} -> {account.balance:.2f} ({account.bank})")
