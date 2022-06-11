import random
def make_deck():

    #set up suits and faces
    arr_suit = ['spades', 'clubs', 'diamonds', 'hearts']

    arr_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    arr_deck = []

    for idx in range(len(arr_suit)):

        string_suit = arr_suit[idx]
        suit_color = " "

        if string_suit == 'spades' or string_suit == 'clubs':
            suit_color = 'black'
        else:
            suit_color = 'red'

        #add face values
        for face_value in arr_faces:
            arr_deck.append({'suit': string_suit, 'color': suit_color, 'face': face_value, 'value': idx + 1})

    return arr_deck

def shuffle_deck(arr_deck):

    arr_hand = []

    for idx in range(5):
        arr_hand.append(random.choice(arr_deck))

    print(arr_hand)







arr_deck = make_deck()
shuffle_deck(arr_deck)
