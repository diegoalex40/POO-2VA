from accountUser import User
from accoutDriver import Driver

class Payment:
    id          = int
    ammount      = int
    user        = User("", "", "", "", "")
    driver      = Driver("", "", "", "", "")
    type        = str

    def __init__(self, id, ammount, user, driver, type):
        self.id      = id
        self.ammount = ammount
        self.user    = user
        self.driver  = driver
        self.type    = type