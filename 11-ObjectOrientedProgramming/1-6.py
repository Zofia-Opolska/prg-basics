class Phone:
    def __init__(self,system,color,battery):
        self.system = system
        self.color = color
        self.battery = battery
        self.is_on = False
    def turn_on(self):
        if self.battery > 0:
            self.is_on = True
            print("Your phone is now on")
        else:
            print("Low battery please charge")
    def turn_off(self):
        if self.is_on == False:
            print("Your device is already turned off")
        else:
            self.is_on = False
            print("Your phone is now off")

my_phone = Phone("Iphone", "Blue", 90)

Phone.turn_on(my_phone)
Phone.turn_off(my_phone)
Phone.turn_off(my_phone)
