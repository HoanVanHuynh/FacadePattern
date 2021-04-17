# Let's develop an application in Python v3.t and implement this use case.
# We start with the client first.
# It's you! Remember, you're the one who has been given
# the responsibility to make sure that the marriage preparations
# are done and the event goes fine!
 
# Let's now move ahead, and talk about the Facade class. 
# As discussed earlier, the Facade class simplifies the interface for the client.
# In this case, EventManager acts as a facade and simplifies the work for you.
# Facade talks to the subsystems and does all the booking and preparations
# for the marriage on your behalf.
# Here is the Python code for the EventManager class: 

class EventManager(object): # facade
    # The EventManger class is the Facade that
    # simplifies the interface for you
    # EventManager uses composition to create objects of
    # the subsystems such as Hotelier, Caterer, and others. 
    def __init__(self):
        print('Event Manager:: Let me talk to the folks\n')

    def arrange(self):
        self.hotelier = Hotelier() 
        self.hotelier.bookHotel() 

        self.florist = Florist() 
        self.florist.setFlowerRequirements() 

        self.caterer = Caterer()
        self.caterer.setCuisine() 

        self.musician = Musician() 
        self.musician.setMusicType() 

# Now that we're done with the Facade and client,
# let's dive into the subsystems. 
# We have developed the following classes for this scenario:
# Hotelier is for the hotel bookings.
# It has a method to check whether the hotel is free on that day (_isAvailable).

class Hotelier(object): # SubSystemClass
    def __init__(self):
        print('Arranging the Hotel for Marriage?---')
    def __isAvailable(self):
        print('Is the Hotel free for the event on given day?')
    def bookHotel(self):
        if self.__isAvailable():
            print('Registered the Booking \n\n')        
# The Florist class is responsible for flower decorations.
# Florist has the setFlowerRequirements() method to be used 
# to set the expectations on the kind of flowers needed for the marriage decoration.

class Florist(object):
    def __init__(self):
        print('Flower Decorations for the Event?')           
    
    def setFlowerRequirements(self):
        print('Carnations, Roses and Lilies would be used for Decorations')
# The Caterer class is used to deal with the caterer and is responsible for the food arrangements.
# Caterer exposes the setCuishine() method to accept the type of cuisine to be served at the marriage.

class Caterer(object):
    def __init__(self):
        print('Food Arrangements for the Event --')

    def setCuisine(self):
        print('Chinese & Continental Cuisine to be served')        
# The Musician class is designed for musical arrangements at the marriage.
# It uses the setMusicType() method to understand music requirements for the event.
class Musician(object):
    def __init__(self):
        print('Musical Arrangements for the Marriage --')        
    def setMusicType(self):
        print('Jazz and Classical will be played')
# However, you're being clever here and passing on the responsibility to the event manager, aren't you?
# Let's now look at the You class. 
# In this example, you create an object of the EventManager class to that the manager can work
# with the relevant folks on marriage preparations while you relax.
class You(object):
    def __init__(self):
        print('You:: Whoa! Marriage Arrangements??!!!')        
    def askEventManager(self):
        print("You:: Let's Contact the Event Manager")
        em = EventManager()
        em.arrange() 
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")
if __name__ == '__main__':
    you = You() 
    you.askEventManager()

# The ouput of the preceding code is given here:
