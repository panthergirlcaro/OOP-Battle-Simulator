from enemy import Enemy
import random

class baby_dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = random.randint(15, 30)
        self.fireee = random.randint(20, 30)

    def cry():
        print("WAHHH WAHHH")
    
    def take_damage(self, damage):
        print("YOU HIT A BABY! YOU MONSTER!!")
        return super().take_damage(damage)
    
    def fire_power(self):
        return 100000

    def attack(self):
        choice = random.choice(["normal", "fireee"])
        if choice == "fireee":
            return self.fireee()
        else:
            if self.health < 50:
                self.attack_power = 75
            elif self.health < 150:
                self.attack_power = 50
            elif self.health < 225:
                self.attack_power = 30
        return random.randint(1, self.attack_power)
