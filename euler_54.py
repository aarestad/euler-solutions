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

hand_type_names = ['High Card', 'One Pair', 'Two Pairs', 'ThreeKind', 'Straight', 'Flush',
					'FullHouse', 'FourOfAKind', 'StraightFlush']

class HandScore:
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

	def __repr__(self):
		return "HandScore(%s, %s)" % (hand_type_names[self.hand_type], self.relevant_ranks)

def get_hand_score(hand):
	card_ranks = sorted(map(ranks.index, [c[0] for c in hand]), reverse=True)
	card_suits = [c[1] for c in hand]

	is_flush = all(x == card_suits[0] for x in card_suits)
	is_straight = all(card_ranks[0] - n == card_ranks[n] for n in range(1, 5))

	if is_straight:
		if is_flush:
			return HandScore(HandType.StraightFlush, card_ranks)
		return HandScore(HandType.Straight, card_ranks)

	if is_flush:
		return HandScore(HandType.Flush, card_ranks)

	rank_counts = {}

	for rank in card_ranks:
		if rank in rank_counts:
			rank_counts[rank] += 1
		else:
			rank_counts[rank] = 1

	if len(rank_counts) == 2: # either 4, 1 or 3, 2
		for rank in rank_counts:
			if rank_counts[rank] == 3:
				other_rank = [r for r in card_ranks if r != rank][0]
				return HandScore(HandType.FullHouse, [rank, rank, rank, other_rank, other_rank])
			if rank_counts[rank] == 4:
				other_rank = [r for r in card_ranks if r != rank][0]
				return HandScore(HandType.FourOfAKind, [rank, rank, rank, rank, other_rank])

	if len(rank_counts) == 3: # 3, 1, 1 or 2, 2, 1
		for rank in rank_counts:
			if rank_counts[rank] == 3:
				other_ranks = [r for r in card_ranks if r != rank]
				return HandScore(HandType.ThreeKind, [rank, rank, rank] + other_ranks)
			if rank_counts[rank] == 2:
				del rank_counts[rank]
				for rank2 in rank_counts:
					if rank_counts[rank2] == 2:
						other_rank = [r for r in card_ranks if r != rank and r != rank2][0]
						higher_pair_rank = max(rank, rank2)
						lower_pair_rank = min(rank, rank2)
						return HandScore(HandType.TwoPairs, [higher_pair_rank, higher_pair_rank, lower_pair_rank, lower_pair_rank, other_rank])

	if len(rank_counts) == 4: # 2, 1, 1, 1
		for rank in rank_counts:
			if rank_counts[rank] == 2:
				other_ranks = [r for r in card_ranks if r != rank]
				return HandScore(HandType.OnePair, [rank, rank] + other_ranks)

	return HandScore(HandType.HighCard, card_ranks)

hands = []

with open('p054_poker.txt') as poker_hands:
	for hand in poker_hands:
		cards = hand.split()
		hands.append((cards[0:5], cards[5:]))

player_1_wins = 0

for hand in hands:
	p1_hand = get_hand_score(hand[0])
	p2_hand = get_hand_score(hand[1])

	if p1_hand > p2_hand:
		player_1_wins += 1

print player_1_wins

# print get_hand_score(["AH", "KH", "QH", "JH", "TH"])
# print get_hand_score(["AH", "KH", "QH", "JD", "TH"])
# print get_hand_score(["AH", "AS", "AC", "AD", "KH"])
# print get_hand_score(["8H", "QH", "TH", "2H", "KH"])
# print get_hand_score(["8H", "8S", "8D", "2H", "2S"])
# print get_hand_score(["8H", "8S", "2D", "2H", "2S"])
# print get_hand_score(["8H", "8S", "8D", "AH", "4S"])
# print get_hand_score(["8H", "8S", "2D", "2H", "4S"])
# print get_hand_score(["8H", "9S", "2D", "2H", "4S"])
# print get_hand_score(["8H", "9S", "2D", "7H", "4S"])
