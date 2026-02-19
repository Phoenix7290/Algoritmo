from collections import deque

def first_move(source, destination, position="start"):
    card = source.popleft()
    if position == "start":
        destination.appendleft(card)
    else:
        destination.append(card)

def sort_cards(cards):
    input_deck = deque(cards)
    sorted_deck = deque()
    buffer = deque()

    while input_deck:
        card = input_deck.popleft()

        while sorted_deck and sorted_deck[0] < card:
            first_move(sorted_deck, buffer, "start")

        sorted_deck.appendleft(card)

        while buffer:
            first_move(buffer, sorted_deck, "start")

    final_deck = deque()
    while sorted_deck:
        first_move(sorted_deck, final_deck, "end")

    return list(final_deck)


# Examplo
if __name__ == "__main__":
    example = [7, 2, 11, 1, 9, 4, 13, 5, 8, 3, 12, 6, 10]
    result = sort_cards(example)
    print(result)