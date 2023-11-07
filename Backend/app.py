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
    'Villager',

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

self.player_dict = {}

for i in range(len(players)):
    newPlayer = Player(players[i], roles[i])
    self.player_dict[players[i]] = newPlayer


self.villagers = []
self.werewolves = []
self.loveBirds = []
self.hoodlumTargets = []
self.cultSects = []
self.protectedPlayers = []


# Segregating and adding character to their respective arrays
for each in self.player_dict:

    if (self.player_dict[each].role in ['Werewolf', 'WolfCub']):
        self.werewolves.append(self.player_dict[each].name)
    elif (self.player_dict[each].role == 'Cult Leader'):
        self.cultLeader = self.player_dict[each].name
    elif (self.player_dict[each].role == 'Cupid'):
        self.cupid = self.player_dict[each].name
    elif (self.player_dict[each].role == 'Hoodlum'):
        self.hoodlum = self.player_dict[each].name
    elif (self.player_dict[each].role == 'Tanner'):
        self.tanner = self.player_dict[each].name
    else:
        self.villagers.append(self.player_dict[each].name)


# iterate for character
# def find_role(self, role):
#     for each in self.player_dict:
#         if (self.player_dict[each].role == playerName):
#             return each


# Function calls for each character

# WereWolves
def werewolves_killing(self):
    print("Werewolves WAKE UP !!, select a player to kill")
    selected_player = int(input())
    return selected_player

# SEER


def seer_selection(self):
    print('Seer WAKE UP !!, Select a player and reveal EVIL/GOOD')
    selected_player = int(input())
    if (selected_player in self.werewolves):
        return "BAD"
    else:
        return "GOOD"


# BodyGuard Protection
def bodyguard_protection(self):
    selected_player = int(input())
    return selected_player


# cupid selections
def cupids_lovers(self):
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


def village_voting(self):
    print("select a player to lynch from village")
    # if village did not select - input 0
    selected_player = int(input())
    if (selected_player):
        self.player_dict[selected_player].life = 0
        eliminated_role = self.player_dict[selected_player].role
        if (eliminated_role == 'Villager'):
            self.villagers.remove(selected_player)
        elif (eliminated_role == 'Wereolf'):
            self.werewolves.remove(selected_player)
        print(eliminated_role + 'is eliminated')


# First Night Scenario
def night_one(self):
    print('Now the Roles are set !!.... VIllAGE SLEEP !!!')

    """
    (what happens at night)
    Werewolves wake up at night 
    Seer Checks 
    bodyguard protects

    """
    getting_killed = self.werewolves_killing()
    print(self.seer_selection())
    getting_protected = self.bodyguard_protection()
    if (getting_killed == getting_protected):
        print("No one is dead")
    else:
        self.player_dict[getting_killed].life = 0
        print(self.player_dict[getting_killed].role + " is dead")


# Day Scenerio
def day(self):
    print('Village Wake Up')
    self.village_voting()


# Game Moderator - Driver
while (len(self.villagers) > len(self.werewolves) or len(self.werewolves) != 0):
    self.night_one()
    self.day()

if (len(self.werewolves) == 0):
    print("Villagers Won !!!")

if (len(self.villagers) == len(self.werewolves)):
    print("WereWolves Won")
