class RedButton:
    def __init__(self):
        self.Schet = 0

    def click(self):
        print("Тревога!") 
        self.Schet += 1
        
    def count(self):
        return self.Schet