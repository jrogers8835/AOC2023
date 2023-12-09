from D07.inputData import inputObj


def convert(card):
    match card:
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 1
        case 'T':
            return 10
        case _:
            return int(card)


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def type(self):
        counts = {}
        jcount = 0
        for card in self.cards:
            if card == 'J':
                jcount += 1
                continue
            if card not in counts:
                counts[card] = 0
            counts[card] += 1
        countTot = [0, 0, 0, 0, 0, 0]
        for c in counts:
            countTot[counts[c]] += 1
        if countTot[5] > 0 or \
                (countTot[3] > 0 and jcount == 2) or \
                (countTot[2] > 0 and jcount == 3) or \
                (jcount > 3):
            return 7
        if countTot[4] > 0 or \
                (countTot[3] > 0 and jcount == 1) or \
                (countTot[2] > 0 and jcount == 2) or \
                (jcount == 3):
            return 6
        if (countTot[3] > 0 and countTot[2] > 0) or \
                (countTot[2] == 2 and jcount == 1) or \
                (countTot[3] > 0 and jcount > 0):
            return 5
        if countTot[3] > 0 or \
                (countTot[2] > 0 and jcount == 1) or \
                (jcount==2):
            return 4
        if countTot[2] == 2 or \
                ( countTot[2] == 1 and jcount == 1):
            return 3
        if countTot[2] > 0 or \
                (jcount == 1):
            return 2
        return 1

    def __str__(self):
        return f'(cards: {self.cards}, bid: {self.bid})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return convert(self.cards[4]) + \
               convert(self.cards[3]) * 1000 + \
               convert(self.cards[2]) * 1000000 + \
               convert(self.cards[1]) * 1000000000 + \
               convert(self.cards[0]) * 1_000000000000

    def __lt__(self, other):
        if self.type() == other.type():
            return self.__hash__() < other.__hash__()
        else:
            return self.type() < other.type()

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)


def run():
    vals = sorted(map(lambda x: Hand(x[0], x[1]), inputObj))
    print(vals)
    vals = list(map(lambda x: x.bid, vals))
    total = 0
    for idx, v in enumerate(vals):
        total += v * (idx + 1)
    print(total)
