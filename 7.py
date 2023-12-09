from collections import Counter

with open("input7.txt") as f:
    lines = f.read().splitlines()

facecard_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

def hand_type(hand, jacks_wild=False):
    """
    7: 5 of a kind
    6: 4 of a kind
    5: full house
    4: 3 of a kind
    3: 2 pair
    2: 1 pair
    1: high card
    """

    if jacks_wild:
        non_jacks = [h for h in hand if h != "J"]
        if len(non_jacks) > 0:
            most_freq = max(set(non_jacks), key=non_jacks.count)
            hand = hand.replace("J", most_freq)
        
    unique_cards = len(set(hand))

    if unique_cards == 1:
        return 7
    if unique_cards == 2:
        if len([c for c in hand if c == hand[0]]) in (1,4):
            return 6
        else:
            return 5
    if unique_cards == 3:
        counter = Counter(hand)
        if max([c for c in counter.values()]) == 3:
            return 4
        else:
            return 3
    if unique_cards == 4:
        return 2
    if unique_cards == 5:
        return 1
    raise Exception

hands = []
for l in lines:
    hand = {}
    # print(f"{l=} {l.split()[0]=} {hand_type(l.split()[0])=}")
    hand["cards"] = l.split()[0]
    hand["cards_scalar"] = [int(facecard_values.get(c, c)) for c in hand["cards"]]
    hand["bid"] = int(l.split()[1])
    hand["type"] = hand_type(hand["cards"])

    hands.append(hand)

# part 1
absolute_rank = len(hands)
s = sorted(hands, key = lambda x: (x["type"], x["cards_scalar"][0], x["cards_scalar"][1], x["cards_scalar"][2], x["cards_scalar"][3], x["cards_scalar"][4]), reverse=True)
winnings = 0

for i in range(0,len(s)):
    # print(absolute_rank, s[i])
    winnings += absolute_rank * s[i]["bid"]
    absolute_rank -= 1

print(f"Part 1: {winnings=}")

# part 2
facecard_values = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
hands = []
for l in lines:
    hand = {}
    hand["cards"] = l.split()[0]
    hand["cards_scalar"] = [int(facecard_values.get(c, c)) for c in hand["cards"]]
    hand["bid"] = int(l.split()[1])
    hand["type"] = hand_type(hand["cards"], jacks_wild=True)

    hands.append(hand)

absolute_rank = len(hands)
s = sorted(hands, key = lambda x: (x["type"], x["cards_scalar"][0], x["cards_scalar"][1], x["cards_scalar"][2], x["cards_scalar"][3], x["cards_scalar"][4]), reverse=True)
winnings = 0

for i in range(0,len(s)):
    winnings += absolute_rank * s[i]["bid"]
    absolute_rank -= 1

print(f"Part 2: {winnings=}")

