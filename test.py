# 2, 3, 4, 5, 6, 7, 8, 9, 10 (T), Jack, Queen, King, Ace.
# 2, 3, 4, 5 ,6, 7, 8, 9, 10    , 11  , 12   , 13  , 14.
from collections import Counter


class Card:
    numbers = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    suits = {"H": 0, "D": 1, "C": 2, "S": 3}

    def __init__(self, number, suit):
        self.n = int(Card.numbers.get(number, number))
        self.s = int(Card.suits.get(suit, suit))

    def compare_num(self, secound_card):
        if self.n == secound_card.n:
            return True
        return False

    def compare_suit(self, secound_card):
        if self.s == secound_card.s:
            return True
        return False


class Hand:
    high_card = 10 ** 0
    one_pair = 10 ** 1
    two_pairs = 10 ** 2
    three_of_a_kind = 10 ** 3
    straight = 10 ** 4
    flush = 10 ** 5
    full_house = 10 ** 6
    four_of_a_kind = 10 ** 7
    straight_flush = 10 ** 8
    royal_flush = 10 ** 9

    def __init__(self, cards):
        self.number = []
        self.suit = []
        for card in cards:
            self.number.append(card.n)
            self.suit.append(card.s)

        self.count_numbers = Counter(self.number)
        self.count_suit = Counter(self.suit)
        self.max_number = max(self.number)
        self.min_number = min(self.number)
        self.score = 0
        print(self.number)

    def score(self):
        self.score += self.highest_card() * Hand.high_card
        pair = self.number_of_pair()
        self.score += pair[0] * Hand.one_pair
            # Hand.two_pairs
            # Hand.three_of_a_kind
            # Hand.straight
            # Hand.flush
            # Hand.full_house
            # Hand.four_of_a_kind
            # Hand.straight_flush
            # Hand.royal_flush


    # Highest value card.
    def highest_card(self):
        return self.max_number

    # Two cards of the same value.
    # Two different pairs.
    def number_of_pair(self):
        pair = [0, 0, 0, 0]
        pair_index = 0
        for i, k in self.count_numbers.items():
            if k == 2:
                pair[pair_index] = i
                pair_index += 1
            if k == 3:
                pair[len(pair)-2] = i
            if k == 4:
                pair[len(pair)-1] = i
        return pair

    # Three cards of the same value
    def three_kind(self):
        for i, k in self.count_numbers.items():
            if k == 3:
                return i
        return 0

    # All cards are consecutive values.
    def straight(self):
        straight = range(self.min_number, self.max_number + 1)
        if list(straight) == sorted(self.number):
            return self.max_number
        return 0

    # All cards of the same suit.
    def flush(self):
        return max(self.count_suit.values())

    # Three of a kind and a pair.
    def full_house(self):
        three = self.three_kind()
        num_pair = 0
        for i in self.number_of_pair():
            if i >= 5:
                num_pair += i
        if three != 0 and num_pair != 0:
            return [three, num_pair]
        return [0, 0]

    # Four cards of the same value.
#    def

    # Straight Flush
    def straight_flush(self):
        for i, k in self.count_suit.items():
            if k == 3:
                return i
        return 0

    # Royal Flush
    def royal_flush(self):
        if self.straight() == 14:
            return 1
        return 0


hand = []
cards = ['8S', 'QH', 'KC', 'TD', 'JS']
for card_info in cards:
    hand.append(Card(card_info[0], card_info[1]))

a = Hand(hand)

print(a.royal_flush())
print(a.full_house())
