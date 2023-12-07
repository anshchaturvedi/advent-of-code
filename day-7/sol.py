from pprint import pprint
from enum import Enum
from collections import Counter
from functools import cmp_to_key

CARD_STRENGTHS = {
  'J': 0,
  '2': 1,
  '3': 2,
  '4': 3,
  '5': 4,
  '6': 5,
  '7': 6,
  '8': 7,
  '9': 8,
  'T': 9,
  'Q': 10,
  'K': 11,
  'A': 12
}

def read_file(filename):
  buffer = []
  with open(filename) as f:
      line = f.readline()
      while line:
          buffer.append(line.strip())
          line = f.readline()

  hands = []
  for line in buffer:
    hand, bid = line.split(' ')
    hands.append(([c for c in hand], int(bid)))
    
  return hands

class HandTypes(Enum):
  HIGH_CARD = 1
  ONE_PAIR = 2
  TWO_PAIR = 3
  THREE_OF_A_KIND = 4
  FULL_HOUSE = 5
  FOUR_OF_A_KIND = 6
  FIVE_OF_A_KIND = 7

def get_best_hand(freqs, num_jokers):
  if freqs == [1, 1, 1, 1, 1]: return [1, 1, 1, 2]

  elif freqs == [1, 1, 1, 2]: 
    if num_jokers == 1: return [1, 1, 3]
    if num_jokers == 2: return [1, 1, 3]

  elif freqs == [1, 2, 2]:
    if num_jokers == 1: return [2, 3]
    if num_jokers == 2: return [1, 4]
  
  elif freqs == [1, 1, 3]:
    if num_jokers == 1: return [1, 4]
    if num_jokers == 3: return [1, 4]
  
  elif freqs == [2, 3]:
    if num_jokers == 2: return [5]
    if num_jokers == 3: return [5]
  
  else: return [5]
  
def get_hand_type(hand):
  counts = Counter(hand)
  freqs = sorted(counts.values())

  num_jokers = counts['J']
  if num_jokers > 0: 
    freqs = get_best_hand(freqs, num_jokers)

  distinct_cards = len(freqs)

  if distinct_cards == 1:
    return HandTypes.FIVE_OF_A_KIND

  elif distinct_cards == 2:
    if freqs == [1, 4]: return HandTypes.FOUR_OF_A_KIND
    if freqs == [2, 3]: return HandTypes.FULL_HOUSE

  elif distinct_cards == 3:
    if freqs == [1, 1, 3]: return HandTypes.THREE_OF_A_KIND
    if freqs == [1, 2, 2]: return HandTypes.TWO_PAIR

  elif distinct_cards == 4:
    return HandTypes.ONE_PAIR
  
  return HandTypes.HIGH_CARD

def group_hands_by_hand(hands):
  grouped_hands = {}
  for hand_type in HandTypes: grouped_hands[hand_type] = []

  for a_hand in hands:
    hand, _ = a_hand
    hand_type = get_hand_type(hand)
    grouped_hands[hand_type].append(a_hand)

  return grouped_hands

def hand_comparator(hand1, hand2):
  (hand1, _), (hand2, _) = hand1, hand2

  for card1, card2 in zip(hand1, hand2):
    if CARD_STRENGTHS[card1] > CARD_STRENGTHS[card2]: return 1
    elif CARD_STRENGTHS[card1] < CARD_STRENGTHS[card2]: return -1

  return 0

def order_hands_by_ranks(grouped_by_hand_type):
  grouped_hands = [group for group in grouped_by_hand_type.values()]

  res = []
  for group in grouped_hands:
    sorted_group = sorted(group, key=cmp_to_key(hand_comparator))
    res.append(sorted_group)

  # flatten using some list comprehension magic
  return [item for sublist in res for item in sublist]

def solution(filename):
  hands = read_file(filename)
  grouped_by_hand_type = group_hands_by_hand(hands)
  ordered_by_ranks = order_hands_by_ranks(grouped_by_hand_type)

  ans = 0
  for idx, hand in enumerate(ordered_by_ranks):
    (_, bid) = hand
    ans += bid * (idx + 1)

  return ans

if __name__ == "__main__":
  small = "input_small.txt"
  large = "input_large.txt"

  print(solution(small))
  print(solution(large))
