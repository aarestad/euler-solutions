hands = []

with open('p054_poker.txt') as poker_hands:
	for hand in poker_hands:
		cards = hand.split()
		hands.append((cards[0:5], cards[5:]))

print hands

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

class HandType:
	HighCard = 0
	OnePair = 1
	TwoPairs = 2
	ThreeKind = 3
	Straight = 4
	Flush = 5
	FullHouse = 6
	FourOfAKind = 7
	StraightFlush = 8

class HandScore
	def __init__(self, hand_type, relevant_ranks):
		self.hand_type = hand_type
		self.relevant_ranks = relevant_ranks # presumed to be the numeric ranks of 0-12

	def __cmp__(self, other):
		if self.hand_type != other.hand_type:
			return -1 if self.hand_type < other.hand_type else 1

		for i in range(len(self.relevant_ranks)):
			if self.relevant_ranks[i] != other.relevant_ranks[i]:
				return -1 if self.relevant_ranks[i] < other.relevant_ranks[i] else 1

		return 0 # tie!

def get_hand_score(hand):
	card_ranks = sorted(map(ranks.index, [c[0] for c in hand]), reverse=True)
	card_suits = [c[1] for c in hand]

	is_flush = all(x == card_suits[0] for x in card_suits)
	is_straight = all(card_ranks[0] == card_ranks[n] - n for n in range(1, 5))

	if is_straight:
		if is_flush:
			return HandScore(HandType.StraightFlush, card_ranks)
		return HandScore(HandType.Straight, card_ranks)

	if is_flush:
		return HandScore(HandType.Flush, card_ranks)

	rank_counts = {}
