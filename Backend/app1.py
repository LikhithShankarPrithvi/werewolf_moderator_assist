import random


class Player:
    def __init__(self, name, role, protection=0, life=1):
        self.name = name
        self.role = role
        self.protection = protection
        self.life = life


players = []
roles = [
    'Werewolf',
    'Werewolf',
    'Werewolf',
    'Cupid',
    'Mentalist',
    'Seer',
    'Cursed',
    'Hoodlum',
    'Tanner',
    'Bodyguard',
    'SpellCaster',
    'Witch',
    'Doppleganger',
    'Cult Leader',
    'Hunter',
    'WolfCub',
]

role_set1 = [
    'Werewolf',
    'Werewolf',
    'Werewolf',
    'Villager',
    'Villager',
    'Villager',
    'Villager',
    'Villager',
    'Villager',
    'Seer',
    'Bodyguard',
    'SpellCaster',
    'Villager',
    'Villager',
    'Villager',
    'Werewolf'
]

print("Hello Village")

print("Take Names of People Playing")

players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# while True:
#     print("Enter Name")
#     name = input()
#     if (name == 'END'):
#         break
#     players.append(name)

random.shuffle(players)
random.shuffle(role_set1)

player_dict = {}

for i in range(len(players)):
    newPlayer = Player(players[i], role_set1[i])
    player_dict[players[i]] = newPlayer


villagers = []
werewolves = []
loveBirds = []
hoodlumTargets = []
cultSects = []
protectedPlayers = []


# Segregating and adding character to their respective arrays
for each in player_dict:
    print(each, player_dict[each].role)
    if (player_dict[each].role == 'Werewolf'):
        werewolves.append(player_dict[each].name)
    # elif (player_dict[each].role == 'Cult Leader'):
    #     cultLeader = player_dict[each].name
    # elif (player_dict[each].role == 'Cupid'):
    #     cupid = player_dict[each].name
    # elif (player_dict[each].role == 'Hoodlum'):
    #     hoodlum = player_dict[each].name
    # elif (player_dict[each].role == 'Tanner'):
    #     tanner = player_dict[each].name
    else:
        villagers.append(player_dict[each].name)


# iterate for character
# def find_role( role):
#     for each in player_dict:
#         if (player_dict[each].role == playerName):
#             return each


# Function calls for each character

# WereWolves
def werewolves_killing():
    print("Werewolves WAKE UP !!, select a player to kill among the bunch")
    for each in villagers:
        if (player_dict[each].life == 1):
            print(each, end=" ")
    selected_player = int(input())
    return selected_player

# SEER


def seer_selection():
    print('Seer WAKE UP !!, Select a player and reveal EVIL/GOOD')
    selected_player = int(input())
    if (selected_player in werewolves):
        return "BAD"
    else:
        return "GOOD"


# BodyGuard Protection
def bodyguard_protection():
    print("protect a player")
    selected_player = int(input())
    return selected_player


# cupid selections
def cupids_lovers():
    print("Select LoveBird 1")
    selected_player1 = int(input())
    print("Select LoveBird 2")
    selected_player2 = int(input())
    loveBirds.append(selected_player1, selected_player2)

# Hoodlum Selections


def hoodlum_Target_selection(player_dict, selected_player1, selected_player2):
    print("Select Target 1")
    selected_player1 = int(input())
    print("Select Target 2")
    selected_player2 = int(input())
    hoodlumTargets.append(selected_player1, selected_player2)

# Check Cupid LoveBirds status


def check_loveBirds(player_dict, loveBirds):
    a, b = loveBirds[0], loveBirds[1]
    if (player_dict[a].life == 0):
        player_dict[b].life = 0
        return b
    elif (player_dict[b].life == 0):
        player_dict[a].life = 0
        return a
    else:
        return 0


# check_hoodlum_status
def hoodlum_hunt(player_dict, hoodlumTargets):
    a, b = hoodlumTargets[0], hoodlumTargets[1]
    if (player_dict[a].life == 0 and player_dict[b].life == 0):
        return 1
    else:
        return 0

# Village Voting


def village_voting():
    print("select a player to lynch from village among the bunch")
    for each in player_dict:
        if (player_dict[each].life == 1):
            print(each, end=" ")
    # if village did not select - input 0
    selected_player = int(input())
    if (selected_player):
        player_dict[selected_player].life = 0
        eliminated_role = player_dict[selected_player].role
        if (eliminated_role == 'Villager'):
            villagers.remove(selected_player)
        elif (eliminated_role == 'Wereolf'):
            werewolves.remove(selected_player)
        print(eliminated_role + 'is eliminated')


# First Night Scenario
def night_one():
    print('Now the Roles are set !!.... VIllAGE SLEEP !!!')

    """
    (what happens at night)
    Werewolves wake up at night 
    Seer Checks 
    bodyguard protects

    """
    getting_killed = werewolves_killing()
    print(seer_selection())
    getting_protected = bodyguard_protection()
    if (getting_killed == getting_protected):
        print("No one is dead")
    else:
        player_dict[getting_killed].life = 0
        print(str(player_dict[getting_killed].name) + ' ,who is a ' +
              player_dict[getting_killed].role + " is dead")


# Day Scenerio
def day():
    print('Village Wake Up')
    village_voting()


# Game Moderator - Driver
print("our werewolves")
print(werewolves)

print("our Villagers")
print(villagers)

while (True):
    night_one()
    day()
    if (len(villagers) == len(werewolves)):
        print("WereWolves Won")
    elif (len(werewolves) == 0):
        print("Villagers Won !!!")
