import random

styles = ("MAGIC","RANGE","MELEE","OTHER")
defense_divisor= 10

class Player:
    def __init__(self, style, strength, attack_speed, defense, accuracy):
        self.combat_style = style
        self.strength = strength
        self.attack_speed = attack_speed
        self.defense = defense
        self.accuracy = accuracy

    combat_style = ""
    style_adv_multiplier = 1
    health = 100
    strength = 1
    attack_speed = 0
    defense = 1
    defense_divisor = 10
    accuracy = 0
    base_rate_damage = 1
        
def determine_advantage(p1, p2):
    #p1 adv
    if(p1.combat_style == 'MAGIC' and p2.combat_style == 'MELEE'):
        p1.style_adv_multiplier = 2
    if(p1.combat_style == 'RANGE' and p2.combat_style == 'MAGIC'):
        p1.style_adv_multiplier = 2
    if(p1.combat_style == 'MELEE' and p2.combat_style == 'RANGE'):
        p1.style_adv_multiplier = 2

    #p2 adv
    if(p1.combat_style == 'MELEE' and p2.combat_style == 'MAGIC'):
        p2.style_adv_multiplier = 2
    if(p1.combat_style == 'RANGE' and p2.combat_style == 'MELEE'):
        p2.style_adv_multiplier = 2
    if(p1.combat_style == 'MAGIC' and p2.combat_style == 'RANGE'):
        p2.style_adv_multiplier = 2

def attack(player, opponent):
    damage_solved = (1 * player.accuracy) * ((player.strength * player.style_adv_multiplier) - (opponent.defense / defense_divisor))
    if damage_solved <= 0:
        print("{0} can't even damage {1}!".format(player.combat_style, opponent.combat_style))
        return -1
    damage_solved += player.base_rate_damage
    hits_required = opponent.health / damage_solved
    total_time = hits_required * (1 / player.attack_speed)
    print("{} took {} seconds to kill {}".format(player.combat_style, total_time, opponent.combat_style))
    return total_time

def run_battle_sim(p1, p2):
    r1 = attack(p1,p2)
    r2 = attack(p2,p1)

    #Edgecase: one or both are weak
    if r1 == -1 and r2 == -1:
        print("They're both too weak to damage each other.")
        return
    if r1 == -1:
        print("P2 " + p2.combat_style + " wins!")
        return
    if r2 == -1:
        print("P2 " + p1.combat_style + " wins!")
        return

    #Determine who won based on total_time
    if (r1 > r2):
        print(p2.combat_style + " wins!")
    elif ( r1 == r2):
        print("Draw")
    else:
        print(p1.combat_style + " wins!")


def create_players():
    p1_style = input("Enter an Attack style for P1: [0 = MAGIC,  1 = RANGE, 2 = MELEE, 3 = OTHER]... ")
    while not p1_style.isnumeric():
        p1_style = input("Please chose one of these styles: [0 = MAGIC,  1 = RANGE, 2 = MELEE, 3 = OTHER]... ")
    while int(p1_style) > 3:
        p1_style = input("Please chose one of these styles: [0 = MAGIC,  1 = RANGE, 2 = MELEE, 3 = OTHER]... ")
    while int(p1_style) < 0:
        p1_style = input("Please chose one of these styles: [0 = MAGIC,  1 = RANGE, 2 = MELEE, 3 = OTHER]... ")
    p1_strength = input("Enter P1 strength level... ")
    while not p1_strength.isnumeric():
        p1_strength = input("Please enter an integer strength level... ")
    p1_attackspeed = input("Enter P1 attack speed level... ")
    while not p1_attackspeed.isnumeric():
        p1_attackspeed = input("Please enter an integer attack speed level... ")
    p1_defense = input("Enter P1 defense level... ")
    while not p1_defense.isnumeric():
        p1_defense = input("Please enter an integer attack speed level... ")
    p1_accuracy = input("Enter P1 accuracy level: [1-100]... ")
    while not p1_accuracy.isnumeric():
        p1_accuracy = input("Please enter an integer accuracy level... ")
    print("Now For P2...")
    p2_style = input("Enter an Attack style for P1: [0 = MAGIC,  1 = RANGE, 2 = MELEE, 3 = OTHER]... ")
    while not p2_style.isnumeric():
        p2_style = input("Please chose one of these styles: [0 = MAGIC,  1 = RANGE, 2 = MELEE, 3 = OTHER]... ")
    while int(p2_style) > 3:
        p1_style = input("Please chose one of these styles: [0 = MAGIC,  1 = RANGE, 2 = MELEE, 3 = OTHER]... ")
    while int(p2_style) < 0:
        p1_style = input("Please chose one of these styles: [0 = MAGIC,  1 = RANGE, 2 = MELEE, 3 = OTHER]... ")
    p2_strength = input("Enter P1 strength level... ")
    while not p1_strength.isnumeric():
        p1_strength = input("Please enter an integer strength level... ")
    p2_attackspeed = input("Enter P1 attack speed level... ")
    while not p2_attackspeed.isnumeric():
        p1_attackspeed = input("Please enter an integer attack speed level... ")
    p2_defense = input("Enter P1 defense level... ")
    while not p1_strength.isnumeric():
        p1_defense = input("Please enter an integer attack speed level... ")
    p2_accuracy = input("Enter P1 accuracy level: [1-100]... ")
    while not p2_accuracy.isnumeric():
        p2_accuracy = input("Please enter an integer accuracy level... ")
    
    if (int(p2_accuracy) > 100):
        p2_accuracy = 100
    if (int(p2_accuracy) < 1):
        p2_accuracy = 1
    if (int(p1_accuracy) > 100):
        p1_accuracy = 100
    if (int(p1_accuracy) < 1):
        p1_accuracy = 1
    if (int(p1_defense) <= 0):
        p1_defense = 100
    if (int(p2_defense) <= 0):
        p2_defense = 1
        
    p1 = Player(styles[int(p1_style)], int(p1_strength), int(p1_attackspeed), int(p1_defense), int(p1_accuracy))
    p2 = Player(styles[int(p2_style)], int(p2_strength), int(p2_attackspeed), int(p2_defense), int(p2_accuracy))
    return p1, p2

def matchup():    
    p1, p2 = create_players()
    determine_advantage(p1,p2)
    run_battle_sim(p1,p2)

if __name__ == '__main__':
    matchup()
