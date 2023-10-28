class Levl():
    def __init__(self, index, bg):
        self.index = index
        self.bg = bg

def change_levl(current):
    return Levl(current.index+1, "red")