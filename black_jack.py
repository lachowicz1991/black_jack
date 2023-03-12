from random import randint, choice
from replit import clear
from art import logo


class BlackJack():
	def __init__(self):
		self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
		self.player_score = 0
		self.dealer_score = 0
		self.player_cards = []
		self.dealer_cards = []

	def play_game(self):
		print(logo)
		is_game_over = False

		for _ in range(2):
			self.player_cards.append(self.deal_card())
			self.dealer_cards.append(self.deal_card())

		while not is_game_over:
			self.player_score = self.calculate_score(self.player_cards)
			self.dealer_score = self.calculate_score(self.dealer_cards)
			print(f"   Your cards: {self.player_cards}, current score: {self.player_score}")
			print(f"   Computer's first card: {self.dealer_cards[0]}")

			if self.player_score == 0 or self.dealer_score == 0 or self.player_score > 21:
				is_game_over = True
			else:
				user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
				if user_should_deal == "y":
					self.player_cards.append(self.deal_card())
				else:
					is_game_over = True

		while self.dealer_score != 0 and self.dealer_score < 17:
			self.dealer_cards.append(self.deal_card())
			self.dealer_score = self.calculate_score(self.dealer_cards)


		print(f"   Your final hand: {self.player_cards}, final score: {self.player_score}")
		print(f"   Computer's final hand: {self.dealer_cards}, final score: {self.dealer_score}")
		print(self.compare())

	def show_score(self):
		print('*Show score*')
		print('Player cards:')
		for card in self.player_cards:
			print(card)
			print(f'Player score:{self.calculate_score(self.player_cards)} \n')

		print('Dealer cards:')
		for card in self.dealer_cards:
			if self.dealer_score < 21 and len(self.dealer_cards):
				print('Hidden card')
			else:
				print(card)
		if self.dealer_score >= 21:
				print(f'Dealer won with score:{self.dealer_score} \n')
		else:
			print('Dealer score:? \n')

	def deal_card(self):
		"""Returns a random card from the deck."""
		card = choice(self.cards)
		return card

	def calculate_score(self, cards):
		"""Take a list of cards and return the score calculated from the cards"""
		if sum(cards) == 21 and len(cards) == 2:
			return 0
		if 11 in cards and sum(cards) > 21:
			cards.remove(11)
			cards.append(1)
		return sum(cards)

	def compare(self):
		clear()
		if self.player_score > 21 and self.dealer_score > 21:
			return "You went over. You lose 😤"
		if self.player_score == self.dealer_score:
			return "Draw 🙃"
		elif self.dealer_score == 0:
			return "Lose, opponent has Blackjack 😱"
		elif self.player_score == 0:
			return "Win with a Blackjack 😎"
		elif self.player_score > 21:
			return "You went over. You lose 😭"
		elif self.dealer_score > 21:
			return "Opponent went over. You win 😁"
		elif self.player_score > self.dealer_score:
			return "You win 😃"
		else:
			return "You lose 😤"

