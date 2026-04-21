import random

class Pokemon:
    def __init__ (self, name, hp, attack_power):
        self.name = name
        self._hp = hp
        self.attack_power = attack_power
    def get_hp(self):
        return self._hp    

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.take_damage(self.attack_power)

    def take_damage(self,amount):
        self._hp -= amount
        if self._hp <= 0:
           self._hp = 0
           print(f"{self.name} has fainted!")
        else: 
           print(f"{self.name} took {amount} damage. HP is now {self._hp}")  

# Fire type Pokemon subclass
class FirePokemon(Pokemon):
    def special_attack(self, target):
        damage = self.attack_power + 5
        print(f"{self.name} uses Flamethrower on {target.name} for {damage} damage!")
        target.take_damage(damage)


# Water type Pokemon subclass
class WaterPokemon(Pokemon):
    def special_attack(self, target):
        damage = self.attack_power + 5
        print(f"{self.name} uses Water Gun on {target.name} for {damage} damage!")
        target.take_damage(damage)


# Battle function
def battle(pokemon1, pokemon2):
    print(f"Battle starts: {pokemon1.name} vs {pokemon2.name}!\n")
    
    round_num = 1
    while pokemon1.get_hp() > 0 and pokemon2.get_hp() > 0:
        print(f"--- Round {round_num} ---")
        
        # Pokemon1 turn: randomly choose normal or special attack
        if random.choice([True, False]) and hasattr(pokemon1, 'special_attack'):
            pokemon1.special_attack(pokemon2)
        else:
            pokemon1.attack(pokemon2)

        if pokemon2.get_hp() <= 0:
            break

        # Pokemon2 turn: randomly choose normal or special attack
        if random.choice([True, False]) and hasattr(pokemon2, 'special_attack'):
            pokemon2.special_attack(pokemon1)
        else:
            pokemon2.attack(pokemon1)

        print()  # spacing between rounds
        round_num += 1

    print("\nBattle ended!")

    


charmander = FirePokemon("Charmander", 39, 10)
squirtle = WaterPokemon("Squirtle", 44, 8)

battle(charmander, squirtle)












