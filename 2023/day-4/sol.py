from pprint import pprint
from collections import defaultdict


def read_file(filename):
    buffer = []
    with open(filename) as f:
        line = f.readline()
        while line:
            buffer.append(line.strip())
            line = f.readline()

    return buffer


def process_cards(cards, part_two=False):
    processed_cards = {}

    for idx, card in enumerate(cards):
        both_parts = list(map(lambda x: x.strip(), card.split("|")))
        first_part = list(map(lambda x: x.strip(), both_parts[0].split(":")))[1]
        second_part = both_parts[1]

        key_set, value_set = [], []
        for num in first_part.split(" "):
            if num != "":
                key_set.append(int(num))
        for num in second_part.split(" "):
            if num != "":
                value_set.append(int(num))

        if part_two:
            processed_cards[idx + 1] = (tuple(key_set), value_set)
        else:
            processed_cards[tuple(key_set)] = value_set

    return processed_cards


def process_cards_and_get_score(cards):
    processed_cards = process_cards(cards)

    total_score = 0
    for my_cards, game_cards in processed_cards.items():
        game_score = 0
        for game_card in game_cards:
            if game_card in my_cards:
                if game_score == 0:
                    game_score = 1
                else:
                    game_score *= 2

        total_score += game_score

    return total_score


def solution(filename):
    cards = read_file(filename)
    ans = process_cards_and_get_score(cards)
    return ans


# --------------------------------- PART 2 ---------------------------------
def process_cards_and_get_score2(cards):
    processed_cards = process_cards(cards, True)

    card_counts = defaultdict(int)
    for key in processed_cards:
        card_counts[key] = 1

    for card_number, cards in processed_cards.items():
        (my_cards, game_cards) = cards

        matching_cards = 0
        for card in game_cards:
            if card in my_cards:
                matching_cards += 1

        current_card_count = card_counts[card_number]
        for i in range(card_number + 1, card_number + 1 + matching_cards):
            card_counts[i] += current_card_count

    ans = 0
    for val in card_counts.values():
        ans += val
    return ans


def solution2(filename):
    cards = read_file(filename)
    ans = process_cards_and_get_score2(cards)

    return ans


if __name__ == "__main__":
    print(solution2("input_small.txt"))
    print(solution2("input_large.txt"))
