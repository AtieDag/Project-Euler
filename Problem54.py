# https://projecteuler.net/problem=54
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
    high_card_value = 10 ** 0
    one_pair_value = 10 ** 1
    two_pairs_value = 10 ** 2
    three_of_a_kind_value = 10 ** 3
    straight_value = 10 ** 4
    flush_value = 10 ** 5
    full_house_value = 10 ** 6
    four_of_a_kind_value = 10 ** 7
    straight_flush_value = 10 ** 8
    royal_flush_value = 10 ** 9

    def __init__(self, players_cards):
        self.number = []
        self.suit = []
        for card in players_cards:
            self.number.append(card.n)
            self.suit.append(card.s)

        self.count_numbers = Counter(self.number)
        self.count_suit = Counter(self.suit)
        self.max_number = max(self.number)
        self.min_number = min(self.number)
        self.score = 0

    def get_score(self):
        # High Card
        self.score += self.highest_card() * Hand.high_card_value
        pair = self.number_of_pair()
        # One Pair
        self.score += pair[0] * Hand.one_pair_value
        # Hand.two_pairs
        self.score += pair[1] * Hand.two_pairs_value
        # Hand.three_of_a_kind
        self.score += pair[2] * Hand.three_of_a_kind_value
        # Hand.straight
        self.score += self.straight() * Hand.straight_value
        # Hand.flush
        # print("flush ", self.flush())
        self.score += self.flush() * Hand.flush_value
        # Hand.full_house
        self.score += self.full_house(pair[2])[0] * Hand.full_house_value
        # Hand.four_of_a_kind
        self.score += pair[3] * Hand.four_of_a_kind_value
        # Hand.straight_flush
        # print("straightflush ",self.straight_flush())
        self.score += self.straight_flush() * Hand.straight_flush_value
        # Hand.royal_flush
        # print("royal_flush ",self.royal_flush())
        self.score += self.royal_flush() * Hand.royal_flush_value
        return self.score

    # Highest value card.
    def highest_card(self):
        return self.max_number

    # Pairs
    def number_of_pair(self):
        """ Returns an array [One Pair, Two Pairs, Three of a Kind,Four of a Kind]
        """
        pair = [0, 0, 0, 0]
        pair_index = 0
        for i, k in self.count_numbers.items():
            if k == 2:
                pair[pair_index] = i
                pair_index += 1
            if k == 3:
                pair[len(pair) - 2] = i
            if k == 4:
                pair[len(pair) - 1] = i
        return pair

    # All cards are consecutive values.
    def straight(self):
        straight = range(self.min_number, self.max_number + 1)
        if list(straight) == sorted(self.number):
            return self.max_number
        else:
            return 0

    # All cards of the same suit.
    def flush(self):
        if max(self.count_suit.values()) == 5:
            return self.max_number
        return 0

    # Three of a kind and a pair.
    def full_house(self, three):
        num_pair = 0
        for i in self.number_of_pair():
            if i >= 5:
                num_pair += i
        if three != 0 and num_pair != 0:
            return [three, num_pair]
        return [0, 0]

    # Straight Flush
    def straight_flush(self):
        if self.straight() > 0:
            for i, k in self.count_suit.items():
                if k == 5:
                    return i
        return 0

    # Royal Flush
    def royal_flush(self):
        if self.straight() == 14:
            return 1
        return 0


def table(dealed_cards):
    player_1 = []
    player_2 = []
    for card_info in dealed_cards.split()[0:5]:
        player_1.append(Card(card_info[0], card_info[1]))

    for card_info in dealed_cards.split()[5:11]:
        player_2.append(Card(card_info[0], card_info[1]))

    player_1_hand = Hand(player_1).get_score()
    player_2_hand = Hand(player_2).get_score()
    print("player 1 score: ", player_1_hand)
    print("player 2 score: ", player_2_hand)
    if player_1_hand > player_2_hand:
        return 1
    if player_1_hand < player_2_hand:
        return 2
    return 0


player_1_wins = 0
player_2_wins = 0
draw = 0
with open("Problem54.txt") as file:
    for line in file:
        winner = table(line)
        if winner == 1:
            player_1_wins += 1
        elif winner == 2:
            player_2_wins += 1
        else:
            draw += 1

print(player_1_wins)
print(player_2_wins)
print(draw)
