class Hero(object):
    def __init__(self):
        self.health = 10
        self.power = 5
    
    def attack(self, enemy):
        enemy.health -= self.power
        print "You do %d damage to the goblin." % barry_the_hero.power
        if steve_the_goblin.health <= 0:
            print "The goblin is dead."
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if steve_the_goblin.health > 0:

    class Goblin(object):
        def __init__(self):
            self.health = 6
            self.power = 2

def main():
    barry_the_hero = Hero()
    steve_the_goblin = Goblin()

    while steve_the_goblin.health > 0 and barry_the_hero.health > 0:
        print "You have %d health and %d power." % (barry_the_hero.health, barry_the_hero.power)
        print "The goblin has %d health and %d power." % (steve_the_goblin.health, steve_the_goblin.power)
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            barry_the_hero.attack(steve_the_goblin)
            # Goblin attacks hero
            barry_the_hero.health -= steve_the_goblin.power
            print "The goblin does %d damage to you." % steve_the_goblin.power
            if barry_the_hero.health <= 0:
                print "You are dead."


main()