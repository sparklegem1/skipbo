import random

CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "skip-bo"]

deck = []

for card in CARDS:
    if card != "skip-bo":
        for i in range(12):
            deck.append(card)
    else:
        for i in range(18):
            deck.append(card)

random.shuffle(deck)

valid_choices = ['dis', 'skip-bo', 'done', 'top', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
loop_counter = 0



class PlayingField:
    def __init__(self):
        self.field = [[0], [0], [0], [0]]



class Player:

    def __init__(self):
        self.hand = []
        self.pile = []
        self.discard = [[], [], [], []]
        self.pile_size = 20

    def create_hand(self, deck):
        for i in range(0, 5):
            card = deck.pop(i)
            self.hand.append(card)


    def create_pile(self, deck):
        for i in range(self.pile_size):
            card = deck.pop(i)
            self.pile.append(card)
        self.top_card = self.pile[0]

    def removed_card(self, card):
        card = self.hand.pop(self.hand.index(card))
        return card


def discard_phase(card, player, col):
    discard_card = player.removed_card(card)
    player.discard[col - 1].append(discard_card)


def player_turn(player1, turn=1):
    global loop_counter, player1_turn, player2_turn


    if len(deck) <= 0 or len(deck) - 5 <= 0 or len(deck) - 4 <=0 or len(deck) - 3 <= 0 or len(deck) - 2 <=0 or len(deck) - 1 <= 0:
        for card in CARDS:
            if card != "skip-bo":
                for i in range(12):
                    deck.append(card)
            else:
                for i in range(18):
                    deck.append(card)

        random.shuffle(deck)


    if len(player1.pile) == 0 and turn == 1:
        print('congratulations (: ')
        player1_turn = False
        player2_turn = False
        return None
    elif len(player1.pile) == 0 and turn == 2:
        print('player 2 wins!!!!')
        return None

    if turn == 1:
        print('PLAYER 1 TURN')
    if turn == 2:
        print('PLAYER 2 TURN')

    #DRAW CARDS UP TO 5 AT START OF TURN
    if len(player1.hand) < 5 and loop_counter == 0:
        for i in range(0, 5 - len(player1.hand)):
            card = deck.pop(i)
            player1.hand.append(card)
    for col in field.field:
        if col != []:
            if col[-1] == 12:
                col.clear()
                col.append(0)
    # LOOP COUNTER MAKES SURE NOT TO DRAW UP TO 5 AFTER START
    loop_counter += 1
    if len(player1.hand) == 0:
        print('You\'re on a roll! Draw 5 more cards and keep going.')
        player1.create_hand(deck)
    player_top_card = player1.pile[0]
    print(f'field: |{field.field[0][-1]}| |{field.field[1][-1]}| |{field.field[2][-1]}| |{field.field[3][-1]}| ')
    print(f'hand: {" ".join([f"|{str(c)}|" for c in player1.hand])}')
    print(f'top card: {player_top_card}  ')
    print(f'discard pile: {player1.discard}')

    # INITIAL INPUT
    player_choice = input('ur turn, type card u wish to play, or'
                          ' type "top" to play your top card, '
                          'type "dis" to play from discard pile, '
                          'or type "done" to discard: ')

    if player_choice not in valid_choices:
        print('this is not a valid move, try again')

    # ENTER DISCARD PHASE
    elif player_choice == 'done':
        print(f'discard: {player1.discard}')
        print(f'hand: {player1.hand}')
        card = input('choose card to discard: ')
        if card in valid_choices[4:]:
            card = int(card)
            if card in player1.hand:
                col = input('choose column to discard to: ')
                if col in valid_choices[4:8]:
                    col = int(col)
                    discard_phase(card, player1, col)
                    print(f'discard: {player1.discard}')
                    loop_counter = 0
                    if turn == 1:
                        player2_turn = True
                        player1_turn = False
                    if turn == 2:
                        player2_turn = False
                        player1_turn = True

                else:
                    print('you picked an invalid column')
            else:
                print('this card is not in your hand')
        elif card == 'skip-bo':
            if card in player1.hand:
                col = input('choose column to discard to')
                if col in valid_choices[4:8]:
                    col = int(col)
                    discard_phase(card, player1, col)
                    loop_counter = 0
                    player2_turn = True
                    player1_turn = False
                else:
                    print('you picked an invalid column')
            else:
                print('this card is not in your hand')

    # PLAY INTEGER FROM HAND
    elif player_choice in valid_choices[4:]:
        player_choice = int(player_choice)
        if player_choice in player1.hand:
            correct_choice = False
            while correct_choice == False:
                col = input('type what column you want to play on, or type 0 to cancel this move: ')
                if col == '0':
                    correct_choice = True
                if col in valid_choices[4:8]:
                    col = int(col)
                    card = player1.removed_card(player_choice)
                    top_card = field.field[col - 1][-1]

                    if card == top_card + 1:
                        field.field[col - 1].append(card)
                        correct_choice = True
                    else:
                        print('cannot play this card here')
                        player1.hand.insert(0, card)

    # PLAY TOP CARD
    elif player_choice == 'top':
        if player_top_card != 'skip-bo':
            correct_choice = False
            while correct_choice == False:
                col = input('type what column you want to play on, or type 0 to cancel this move: ')
                if col == '0':
                    correct_choice = True
                if col in valid_choices[4:8]:
                    col = int(col)
                    card = player1.pile.pop(0)
                    top_card = field.field[col - 1][-1]

                    if card == top_card + 1:
                        field.field[col - 1].append(card)
                        correct_choice = True
                    else:
                        print('cannot play this card here')
                        player1.pile.insert(0, card)
                else:
                    print('invalid column')
        elif player_top_card == 'skip-bo':
            correct_choice = False
            while correct_choice == False:
                choice = input('choose the value of the skip-bo card: ')
                if choice not in valid_choices[4:]:
                    print('please choose a valid choice')
                else:
                    choice = int(choice)
                    player1.pile[0] = choice
                    col = input('type what column you want to play on, or type 0 to cancel this move: ')
                    if col == '0':
                        correct_choice = True
                    if col in valid_choices[4:8]:
                        col = int(col)
                        card = player1.pile.pop(0)

                        # TOP CARD IN THIS INSTANCE IS TOP CARD ON THE PLAYING FIELD
                        top_card = field.field[col - 1][-1]
                        if card == top_card + 1:
                            field.field[col - 1].append(card)
                            correct_choice = True
                        else:
                            print('invalid card')
                            correct_choice = True
                    else:
                        print('invalid column')

    # PLAY SKIP BO FROM HAND
    elif player_choice == 'skip-bo':
        correct_choice = False
        while correct_choice == False:
            value = input('choose the value of the skip-bo card: ')
            if value not in valid_choices[4:]:
                print('please choose a valid choice')
            else:
                value = int(value)
                col = input('type what column you want to play on, or type 0 to cancel this move: ')
                if col == '0':
                    correct_choice = True
                if col in valid_choices[4:8]:
                    col = int(col)
                    top_card = field.field[col -1][-1]
                    if value == top_card + 1:
                        index = player1.hand.index('skip-bo')
                        player1.hand[index] = value
                        card_in_play = player1.hand[index]
                        field.field[col - 1].append(card_in_play)
                        correct_choice = True
                    else:
                        print('cannot play this card here')
                        correct_choice = True
                else:
                    print('not a valid column')

    # PLAY FROM DISCARD
    elif player_choice == 'dis':
        correct_choice = False
        while not correct_choice:
            print(player1.discard)
            card = input('choose which discard pile to play from (this plays your last card in the pile), press either 1,2,3 or 4: ')
            if card in valid_choices[4:8]:
                card = int(card)
                if player1.discard[card - 1] == []:
                    print('this stack is empty')
                elif player1.discard[card - 1][-1] == 'skip-bo':
                    value = input('please choose value of skip-bo card: ')
                    if value in valid_choices[4:]:
                        value = int(value)
                        col = input('select column on press 0 to cancel')
                        if col == '0':
                            correct_choice = True
                        if col in valid_choices[4:8]:
                            col = int(col)
                            if field.field[col - 1][-1] + 1 == value:
                                player1.discard[card - 1][-1] = value
                                card_in_play = player1.discard[card - 1].pop(-1)
                                field.field[col - 1].append(card_in_play)
                                correct_choice = True
                else:
                    col = input('type what column you want to play on, or type 0 to cancel this move: ')
                    if col == '0':
                        correct_choice = True
                    if col in valid_choices[4:8]:
                        col = int(col)
                        stack_in_play = player1.discard[card - 1]
                        top_card = field.field[col - 1][-1]
                        if stack_in_play[-1] == top_card + 1:
                            card_in_play = stack_in_play.pop(-1)
                            field.field[col - 1].append(card_in_play)
                            correct_choice = True
                        else:
                            print('cannot play this card here')
            else:
                print('please choose a valid card')



# CREATE PLAYERS
player1 = Player()
player1.create_hand(deck)
player1.create_pile(deck)
player2 = Player()
player2.create_hand(deck)
player2.create_pile(deck)
field = PlayingField()


game = True
player1_turn = True
player2_turn = False

print('SKIP-BO!!!!')
rules = input('would you like to see the rules? y/n ')
if rules == 'y':
    print('How to Play Skip-Bo: Each player starts with 5 cards in their hand. On the field there are four slots,\n'
          ' each slot will be empty at first and show a zero. You will select a card either from your hand,\n'
          ' discard pile or main pile and play it on a slot of your choice in the field, but you will only be able \n'
          'to play your card if it\'s value is one higher than the card in the slot you\'ve chosen\n'
          'Therefore, the first card played must be a 1 or a "skip-bo". If you cannot play a card, \n'
          'type done and you will be asked to discard. You have 4 discard piles. You may discard any card into any \n'
          'pile, but be aware that if you want to play one of those cards later on you will only be able to play the \n'
          'top card on the pile (the card furthest to the right in the pile). Cards labeled "skip-bo" are wild cards \n'
          'and their values can be changed to whichever value necessary to be played. In addition to a hand and a \n'
          'discard pile, each player also has a main pile in which only the top card is revealed. It is labelled as \n'
          '"top-card". The goal of the game is to get rid of all the cards in this pile, and will be prompted at the \n'
          'beginning of the game to choose the size of this pile. So bear this in mind when playing, as it is always \n'
          'smarter to play your "top-card" when possible in order to dissipate your main pile as quickly as possible.\n'
          'Remember you may also play from your discard pile if you wish, simply type "dis" and follow the prompts. \n'
          'Also, if you run out of cards in your hand before discarding, you get to draw 5 more cards and keep going!\n'
          'Hopefully this is enough info to get started, happy SKIP-BO TIME!!!!!!!!!')

pile_size = False
while pile_size == False:
    choose_pile_size = input('Choose pile size, type 5, 10, 15, or 20: ')
    if choose_pile_size in ['5', '10', '15', '20']:
        choose_pile_size = int(choose_pile_size)
        player1.pile_size = choose_pile_size
        player2.pile_size = choose_pile_size
        pile_size = True
    else:
        print('invalid pile size')

cpu = Player()
cpu.create_hand(deck)
cpu.create_pile(deck)

def can_play(player_card, field_card):
    if player_card == field_card + 1:
        return True
    else:
        return False




while game:

    while player1_turn == True:
        if len(player1.pile) == 0:
            print('player 1 wins!')
            game = False
        if len(player2.pile) == 0:
            print('player 2 wins!')
            game = False
        else:
            player_turn(player1, turn=1)

    while player2_turn == True:
        if len(player1.pile) == 0:
            print('player 1 wins!')
            game = False
        if len(player2.pile) == 0:
            print('player 2 wins!')
            game = False
        else:
            player_turn(player2, turn=2)









"""


PLAYER TURN:
IF PLAYER 
CHECK IF START OF TURN AND DRAW UP TO FIVE CARDS
IF NOT START OF TURN CHECK IF HAND == 0
IF HAND == 0 THEN DRAW 5 CARDS
ELSE:
PLAY NUMERIC CARD, OR PLAY SKIP-BO (WILD), OR DISCARD
IF NUMERIC CARD IS SELECTED, CHECK IF CARD IS ABLE TO BE PLAYED AT A SELECTED COLUMN AND PLAY IT
IF SKIP-BO IS SELECTED
IF DISCARD IS SELECTED, DISCARD AND MOVE TO NEXT PLAYERS TURN. 



"""