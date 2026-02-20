class nimal:
    #Method
    def eat(self):
        print("Animal is Eating")

    def sleep(self):
        print("Animal is Sleeping")
    #predtor : Tiger, Lion
    class predtor(Animal):
        def hunt(self):
            print("Predator is Hunting")
    # prey : Rabit Cow
    class prey:
        def escape(self):
            print("Prey is escaping")
    #Create Objectes
    #lin is Predator
    lin = predtor()
    lin.hunt()
    lin.sleep()
    lin.eat()
    lin.escape()

    #Rabit is Prey
    rabit = prey()
    rabit.eat()
    rabit.sleep()
    rabit.escape()
    