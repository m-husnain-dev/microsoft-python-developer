class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def reduce_health(self, by):
        self.health -= by
        print(f"{self.name} now has {self.health} health.")

# DSL-like functions for Character creation
def create_character(name, health, strength):
    return Character(name, health, strength)

def create_enemy(name, health, strength):
    return Character(name, health, strength)

# DSL-like function for actions
def when(action_description, action_function):
    print(f"Action: {action_description}")
    action_function()

# Named function for the action
def hero_attack_goblin():
    goblin.reduce_health(by=hero.strength)

# Example usage (DSL-like):
hero = create_character(name="Hero", health=100, strength=50)
goblin = create_enemy(name="Goblin", health=20, strength=10)

when("Hero attacks Goblin", hero_attack_goblin)