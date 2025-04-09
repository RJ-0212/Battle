import random

class Player:
    def __init__(self, name):
        self.name = name
        self.HP = 500
        self.A = -200
        self.B = random.choice([-100, -300])


class Warrior(Player):
    def W_defend(self, attack):
        block = 0.5
        dodge = random.choice([True, False])
        if attack=="A":
            print(f"{npc.name} uses its claws!!")
        else:
            print(f"{npc.name} spits deadly venom!!")

        defend = input("Choose your move(A)Dodge(B)Block").upper()
        if defend=="A":
            defend_result="dodge"
        else:
            defend_result="block"
        return {'block':block,'dodge':dodge,'defend_result':defend_result}
    def W_attack(self,npc):
        attack111=input("Choose your move(A)Thrust(B)Swing and Slash").upper()
        if attack111=="A":
            print(f"{player1.name} uses Thrust attack!!")
            if npc.T_defend()['defend_result']=='dodge':
                if npc.T_defend()['dodge']==True:
                    print(f"Troll dodges your attack! No damage taken! HP={npc.HP}")
                else:
                    npc.HP +=player1.A
                    print(f"Troll takes full damage! HP={npc.HP}")
            else:
                npc.HP += self.A*npc.T_defend()["block"]
                print(f'Troll blocks your attack! HP={npc.HP}')
        else:
            print(f"{player1.name} uses Swing and Slash!!")
            if npc.T_defend()['defend_result'] == 'dodge':
                if npc.T_defend()['dodge'] == True:
                    print(f"Troll dodges your attack! No damage taken! HP={npc.HP}")
                else:
                    npc.HP += player1.B
                    print(f"Troll takes full damage! HP={npc.HP}")
            else:
                npc.HP += player1.B*npc.T_defend()['block']
                print(f'Troll blocks your attack! HP={npc.HP}')

class Troll(Player):
    def T_defend(self):
        dodge = random.choice([True, False])
        block=0.5
        defend_result=random.choice(['block','dodge'])
        return {'defend_result':defend_result,'dodge': dodge,'block':block}
    def T_attack(self,player1):
        attack=random.choice(["A","B"])
        w_defense_result = player1.W_defend(attack)

        if attack=="A":
            if w_defense_result['defend_result']=="dodge":
                if w_defense_result['dodge']:
                    print(f"{player1.name} dodges the attack! No damage taken! HP={player1.HP}")
                else:
                    player1.HP += npc.A
                    print(f"{player1.name} takes full damage! HP={player1.HP}")
            else:
                player1.HP += npc.A*w_defense_result['block']
                print(f'{player1.name} blocks the attack! HP={player1.HP}')
        if attack=="B":
            if w_defense_result['defend_result'] == "dodge":
                if w_defense_result['dodge']:
                    print(f"{player1.name} dodges the attack! No damage taken! HP={player1.HP}")
                else:
                    player1.HP += npc.B
                    print(f"{player1.name} takes full damage! HP={player1.HP}")
            else:
                player1.HP += npc.A*w_defense_result['block']
                print(f'{player1.name} blocks the attack! HP={player1.HP}')





npc=Troll("Troll")
print("OH NO!! The Troll is taking over the village!")
start = input("Warrior, the town needs you! Counterattack?(A)Yes(B)No").upper()

if start == "B":
    print("Game Over.")
else:
    name1 = input("Enter your name:")
    player1 = Warrior(name1)

    while True:
        player1.W_attack(npc)
        npc.T_attack(player1)



        if npc.HP<=0:
            print("!!!VICTORY!!!")
            break
        elif player1.HP<=0:
            print("-----DEFEAT-----")
            break
