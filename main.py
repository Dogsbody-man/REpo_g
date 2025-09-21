class Character:
    def __init__(self, level: int):
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int):
        damage = damage - (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -= damage

    def is_alive(self) -> bool:
        return self.health_points > 0
    
    def get_defence(self):
        defence = self.base_defence * self.level
        return defence

    def __str__(self):
        return f"{self.name_character} (level {self.level}), hp : {self.health_points}"

class Ork(Character):

    base_health_points = 100
    base_attack_power = 10
    base_defence = 15
    name_character = 'Ork'

    @property
    def defence(self):
        defence = super().defence
        if self.health_points < 50:
            defence *= 3
        return defence

class Elf(Character):

    base_health_points = 50
    base_attack_power = 15
    base_defence = 10
    name_character = 'Elf'

def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
        
    print(f"Character 1: {character_1}, is_alive: {character_1.is_alive()}")
    print(f"Character 2: {character_2}, is_alive: {character_2.is_alive()}")

ork = Ork(level=5)
elf = Elf(level=6)

fight(character_1=ork, character_2=elf)