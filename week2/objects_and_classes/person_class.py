class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def __repr__(self):
        return '' % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        
    
    def print_contact_info(self):
        print "%s\'s email: %s, %s\'s phone number: %s" % (self.name, self.email, self.name, self.phone)
    
    def add_friend(self, friend):
        self.friends.append(friend.name)

    def num_friends(self):
        return len(self.friends)


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

jordan.friends.append(sonny)
sonny.friends.append(jordan)

#print sonny.greet(jordan)
#print jordan.greet(sonny)

#print Person.print_contact_info(sonny)

#number of friends that jordan has
#print len(jordan.friends) = #print jordan.num_friends()
  
#adding a the friend sonny to jordans friends list
#print jordan.add_friends.append(sonny) = #print jordan.add_friend(sonny)
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
print sonny.greeting_count