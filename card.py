#definition for a card class

class Card:
    def _init_(self, new_suit, new_rank):
        self.suit = new_suit
        self.rank = new_rank
        self.value = 0
        if new_rank == "Two":
            self.value = 2
        elif new_rank == "Three":
            self.value = 3
        elif new_rank == "Four":
            self.value = 4
        elif new_rank == "Five":
            self.value = 5
        elif new_rank == "Six":
            self.value = 6
        elif new_rank == "Seven":
            self.value = 7
        elif new_rank == "Eight":
            self.value = 8
        elif new_rank == "Nine":
            self.value = 9
        elif new_rank == "Ten":
            self.value = 10
        elif new_rank == "Jack":
            self.value = 10
        elif new_rank == "Queen":
            self.value = 10
        elif new_rank == "King":
            self.value = 10
        elif new_rank == "Ace":
            self.value = 11
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def get_value(self):
        return self.value
    def __str__(self):
        result = f"{self.rank} of {self.suit}"
        return result
    def change_ace(self):
        if self.suit == "Ace" and self.value == 11:
            self.value = 1
            return True
        else: 
            return False
    
