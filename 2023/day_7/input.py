from enum import IntEnum, auto
from collections import Counter
from dataclasses import dataclass


class HandType(IntEnum):
    HighCard = auto()
    OnePair = auto()
    TwoPair = auto()
    ThreeOfAKind = auto()
    FullHouse = auto()
    FourOfAKind = auto()
    FiveOfAKind = auto()


@dataclass
class Hand:
    cards: str
    bid: int
    hand_type: HandType
    cards_set: str = "23456789TJQKA"    

    def __lt__(self, other: "Hand"):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for self_card, other_card in zip(self.cards, other.cards):
            if self_card != other_card:
                return self.cards_set.index(self_card) < self.cards_set.index(other_card)


def read_file_as_lines(filename: str = "input") -> list[str]:
    with open(filename, "r") as f:
        return list(map(str.strip, f))


def get_hand_type(cards: str) -> str:
    cards: Counter = Counter(cards)
    most_common_cards = cards.most_common(2)
    if most_common_cards[0][1] == 5:
        return HandType.FiveOfAKind
    if most_common_cards[0][1] == 4:
        return HandType.FourOfAKind
    if most_common_cards[0][1] == 3:
        if most_common_cards[1][1] == 2:
            return HandType.FullHouse
        return HandType.ThreeOfAKind
    if most_common_cards[0][1] == 2:
        if most_common_cards[1][1] == 2:
            return HandType.TwoPair
        return HandType.OnePair
    return HandType.HighCard


def change_joker_to_match_the_best_set(cards: str) -> str:
    cards_counter: Counter = Counter(cards)
    for most_common_card, _ in cards_counter.most_common(2):
        if most_common_card != "J":
            break
    return cards.replace("J", most_common_card)


def part_1() -> str:
    lines = read_file_as_lines()
    hands = []
    total_winnings = 0
    for line in lines:
        cards, bid = line.split()
        hand_type = get_hand_type(cards)
        hands.append(Hand(cards, int(bid), hand_type))
    hands.sort()
    for rank, hand in enumerate(hands, 1):
        total_winnings += rank * hand.bid

    return f"The result for part 1 is {total_winnings}"


def part_2() -> str:
    lines = read_file_as_lines()
    hands = []
    total_winnings = 0
    for line in lines:
        cards, bid = line.split()
        hand_type = get_hand_type(change_joker_to_match_the_best_set(cards))
        hands.append(Hand(cards, int(bid), hand_type, cards_set="J23456789TQKA"))
    hands.sort()
    for rank, hand in enumerate(hands, 1):
        total_winnings += rank * hand.bid

    return f"The result for part 2 is {total_winnings}"


def main() -> None:
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
