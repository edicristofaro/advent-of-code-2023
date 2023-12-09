with open("input4.txt") as f:
    lines = f.read().splitlines()

# part 1
card_points = []
total_points = 0
for l in lines:
    card = l.split(":")[1]
    winning_numbers = [int(n) for n in card.split("|")[0].split(" ") if n.isdigit()]
    card_numbers = [int(n) for n in card.split("|")[1].split(" ") if n.isdigit()]

    card_winners = [c for c in card_numbers if c in winning_numbers]
    if len(card_winners) > 0:
        total_points += 2**(len(card_winners)-1)
    
    # output this for part 2
    card_points.append(len(card_winners))

# part 2

def count_cards(cards, index):
    total_cards = 0
    for i, card in enumerate(cards):
        if card > 0 and i+index <= len(card_points):
            total_cards += count_cards(card_points[i+index+1:i+index+card+1], i+index+1) + 1
        else:
            total_cards += 1
    
    return total_cards
    
print(count_cards(card_points, 0))


