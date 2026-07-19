# oop enables us to make user made data type

# class and objects

# class is a blueprint
# 2types class --builtin , userdefind


# atm machine


class Atm:
    # constructor is special fun ->

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        hi how can i help
        press 1 to create pin
        press 2 to change pin
        3 to balance
        4 to withdraw
        any else to exit
              """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("enter pin")
        self.pin = user_pin

        user_balance = int(input("enter balance"))
        self.balance = user_balance

        print("pin created bro")
        self.menu()

    def change_pin(self):
        old_pin = input("enter old pin")
        if old_pin == self.pin:
            # change
            new_pin = input("enter new pin")
            self.pin = new_pin
            print("pin changed ok")
        else:
            print("wrong old pin")

        self.menu()

    def check_balance(self):
        user_pin = input("enter pin")

        if user_pin == self.pin:
            print("your balance is", self.balance)
        else:
            print("bhai no")

        self.menu()

    def withdraw(self):
        user_pin = input("enter pin")
        if user_pin == self.pin:
            amount = int(input("enter amt"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("withdraw done , balance is", self.balance)

            else:
                print("gareeb")

        else:
            print("wrong pass bhai")

        self.menu()


myatm = Atm()
