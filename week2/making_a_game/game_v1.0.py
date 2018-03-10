# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character(object):
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        print "You do %d damage to the goblin." % self.power

class Hero(Character):
    #def __repr__(self):
        return '' % (self.enemy)
        
    def __init__(self):
        self.health = 10
        self.power = 5

    #def attack(self, enemy):
     #   enemy.health -= self.power
     #   print "You do %d damage to the %s." % (self.power, self.enemy)
        
    # def alive(self):
    #     if self.health <= 0:
    #         #print "The hero is dead."
    #         return False
    #     else:
    #         return True

    def status(self):
         print "You have %d health and %d power." % (self.health, self.power)


class Goblin(object):
    def __init__(self):
        self.health = 6
        self.power = 2
    
    def attack(self, enemy):
        enemy.health -= self.power
        print "You do %d damage to the hero." % self.power
    
    # def alive(self):
    #     if self.health <= 0:
    #         #print "The goblin is dead."
    #         return False
    #     else:
    #         return True

    def status(self):
         print "Goblin have %d health and %d power." % (self.health, self.power)
    

def main():
    hero = Hero()
    
    goblin = Goblin()
    
    while goblin.alive() and hero.alive():
        goblin.status()
        hero.status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
        


main()
