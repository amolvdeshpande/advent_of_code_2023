import re
import functools
import collections

with open('input.txt') as f:
    hands = [(hand.split()[0], int(hand.split()[1])) for hand in f.readlines()]

def find_rank(hand):
    c = collections.Counter(list(hand))
    if c['J'] > 0:
        most_common = c.most_common()[0][0]
        if most_common == 'J' and len(c) > 1:
            most_common = c.most_common()[1][0]
        else:
            most_common = c.most_common()[0][0]
        hand_r = hand.replace('J', most_common)
        c = collections.Counter(list(hand_r))
        print(hand + " -> " + hand_r)

    if len(c) == 1:
        return 10
    elif len(c) == 2:
        if c.most_common()[0][1] == 4:
            return 9
        else:
            return 8
    elif len(c) == 3:
        ## 3 of a kind, or 2 pairs
        if c.most_common()[0][1] == 3:
            return 7
        else:
            return 6
    elif len(c) == 4:
        return 5
    else:
        return 4

def compare_cards(card1, card2):
    if card1 == 'J':
        return -1
    if card2 == 'J':
        return 1

    if (card1, card2) in [('T', 'J'), ('T', 'Q'), ('T', 'K'), ('T', 'A'), ('J', 'Q'), ('J', 'K'), ('J', 'A'), ('Q', 'K'), ('Q', 'A'), ('K', 'A')]:
        return -1
    elif card1 in ['T', 'J', 'Q', 'K', 'A']:
        return 1
    elif card2 in ['T', 'J', 'Q', 'K', 'A']:
        return -1
    else:
        return int(card1) - int(card2)

def compare_hands(hand1, hand2):
    rank1, rank2 = find_rank(hand1[0]), find_rank(hand2[0])
    if rank1 != rank2:
        return rank1 - rank2
    else:
        # find first character that differs
        for i in range(len(hand1[0])):
            if hand1[0][i] != hand2[0][i]:
                return compare_cards(hand1[0][i], hand2[0][i])
        print("comparing " + hand1[0] + " and " + hand2[0])
        assert False
        return 0


sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands))
    
total = 0

for i in range(len(sorted_hands)):
    total += sorted_hands[i][1] * (i+1)

print(total)
