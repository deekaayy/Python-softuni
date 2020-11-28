class Wizard:
    def __init__(self, name:str, hp: int, damage:int):
        self.name = str(name)
        self.hp = int(hp)
        self.damage = int(damage)

    def __str__(self):
        return f"Wizard: {self.name}. Health: {self.hp}. Damage power: {self.damage}"

wiz_list = []
data = input().split()

while not (data[0] == "fight" or data[0] == "end"):
    if data[0] == "new":
        if not any(x.name == data[1] for x in wiz_list):
            wizard = Wizard(data[1], int(data[2]), int(data[3]))
            wiz_list.append(wizard)
        else:
            print("Wizard already exists!")
    elif data[0] == "edit":
        if any(x.name == data[1] for x in wiz_list):
            for wizard in wiz_list:
                if wizard.name == data[1]:
                    wizard.hp += int(data[2])
                    wizard.damage += int(data[3])
        else:
            print("Wizard does not exist!")

    data = input().split()


while not data[0] == 'end':
    if len(data)>1:
        fighters = data
        fighters.remove("<=>")
        if len(fighters)>1:
            if any(x.name == data[0] for x in wiz_list) and any(x.name == data[1] for x in wiz_list):
                wiz1 = list(filter(lambda wizerd: wizerd.name == fighters[0], wiz_list))[0]
                wiz2 = list(filter(lambda wizerd: wizerd.name == fighters[1], wiz_list))[0]
                wiz1.hp += 50
                if wiz2.hp - int(wiz1.damage) <=0:
                    print(f"Fatality - {wiz1.name} wins!")
                    wiz_list.remove(wiz2)
                else:
                    wiz2.hp -= int(wiz1.damage)
                    print(f"Next time {wiz2.name}!")
            else:
                print(f"Cannot place a fight with non-existing wizards!")
        else:
            print(f"Cannot place a fight with non-existing wizards!")

    data = input().split()


survivors = sorted(wiz_list, key= lambda wz: -wz.hp)

for wiz in survivors:
    print(wiz)
