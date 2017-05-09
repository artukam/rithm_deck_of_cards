from random import shuffle
from inspect import getargspec
import csv

class Card():
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
	
	def __str__(self):
	  return "The {} of {}".format(self.value,self.suit)

def log_function(fn):
	def inner(*args):
		with open("deck.txt", "a+") as file:
			file.write(fn.__name__)
			print(fn.__name__)
		return fn(*args)
	return inner


class Deck():
	def __init__(self):
		suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
		values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
		self.deck_value = [Card(suit,value) for suit in suits for value in values]
		self.burn = []

	@log_function
	def shuffle_deck(self):
		shuffle(self.deck_value)
		return self.deck_value

	@log_function
	def deal_card(self):
		if len(self.deck_value) == 0:
		  return "No cards left"
		else:
		  return self.deck_value.pop(0)
	
	def __str__(self):
	    return "Pick a card, any card"

	def __iter__(self):
		self.__i = -1
		return self

	def __next__(self):
		if self.__i<len(self.deck_value)-1:
			self.__i += 1
			return self.deck_value[self.__i]
		else:
			raise StopIteration
	
	def save_game(self):
		with open("deck_one.csv", "w+") as csvfile:
			data = ["suit", "value"]
			card_writer = csv.DictWriter(csvfile, fieldnames=data)
			card_writer.writeheader()
			for val in self.deck_value:
				card_writer.writerow({
					"suit": val.suit,
					"value": val.value
					})

	def reload_game(self):
		with open("deck_one.csv") as csvfile:
			card_reader = csv.DictReader(csvfile)
			rows = list(card_reader)
			self.deck_value = [Card(num["suit"],num["value"]) for num in rows]


	  
class Player():
  	def __init__(self, name, buy_in):
  		self.name = name
  		self.buy_in = buy_in
  		self.hand = []
  
jack = Player("Jack",1000)
thomas = Player ("Thomas",2000)

x = Deck()
x.shuffle_deck()
x.deal_card()
x.deal_card()
x.deal_card()
x.deal_card()
x.save_game()
x.reload_game()

for val in x.deck_value:
	print(val)




