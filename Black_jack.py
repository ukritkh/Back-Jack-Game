"""

Name: Ukrit khonglao  Username: ukho367  ID number: 677644555 

"""
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        try:
            result = self.items.pop()
        except IndexError:
            result = 'The queue is empty.'
        return result

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return (self.items == [])
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        try:
            result = self.items.pop()
        except IndexError:
            result = 'Pop Error: The stack is empty!'
        return result
	
class PokerCard:
    def __init__(self, item):
        self.card = item
        self.value = self.__evaluate(item)
    
    def __str__(self):
        return (self.card)
    
    def __evaluate(self, item):
        #read every element in the deck
        for i in range(len(item)):
            card = item[i]
            card_value = card[0]
            #check if it is a digit card otherwise return the its value
            if card_value.isdigit():
                return card_value
            elif card_value == "T" or card_value == "J" or card_value == "Q" or card_value == "K":
                return 10
            #if it is an A then the value is 11
            elif card_value == "A":
                return 11

class Deck:
    def __init__(self):     
        self.cards = Stack()      
        cardlist = ['AS', 'AH', 'AC', 'AD', '2S', '2H', '2C', '2D', '3S', '3H', '3C', '3D', '4S', 
                    '4H', '4C', '4D', '5S', '5H', '5C', '5D',  '6S', '6H', '6C', '6D', '7S', '7H','7C', 
                    '7D', '8S', '8H', '8C', '8D', '9S', '9H', '9C', '9D', 'TS', 'TH', 'TC', 'TD', 'JS', 
                    'JH', 'JC', 'JD', 'QS', 'QH', 'QC', 'QD', 'KS', 'KH', 'KC', 'KD'] 
        
        for i in range(52):
            #insert every element in the cardlist to Stack
            self.cards.push(cardlist[i])
    def __str__(self):
        cards_string = ""
        count = 0
        for row in range(0,52):
            cards_string += str(self.cards.items[row]) + " "
            count += 1
            # make sure they are 13 cards each row
            if count == 13:
                #enter a new row after 13 cards
                cards_string += "\n"
                count = 0
        return cards_string
    
    def shuffleONE(self, no):
        #create a variable a deck of cards
        deck_cards = self.cards.items
        s1 = []
        s2 = []
        #remove the last card from the deck by no number and add in Stack s1
        #first card that is draw or pop will be on the top of the s1 deck
        for i in range(no):
            pop_s1 = deck_cards.pop()
            s1.append(pop_s1)
        #remove the rest of the cards from the deck by length of the deck and add in Stack s2
        #each card that is draw or pop will be on the top of the s2 deck
        for i in range(len(deck_cards)):
            pop_s2 = deck_cards.pop()
            s2.append(pop_s2)
        #add cards one by one from Stack s1 first and s2 follow, back to the deck
        while len(deck_cards) < 52:
            #if there are still cards both s1 and s2, then put one by one into the deck
            if s1 != [] and s2 != []:
                pop_s1 = s1.pop()
                pop_s2 = s2.pop()
                self.cards.push(pop_s1)
                self.cards.push(pop_s2)
            #if cards in s1 is empty then add only cards from s2 back to the deck 
            if s1 == [] and s2 != []:
                pop_s2 = s2.pop()
                self.cards.push(pop_s2)
            #if cards in s2 is empty then add only cards from s1 back to the deck
            if s2 == [] and s1 != []:
                pop_s1 = s1.pop()
                self.cards.push(pop_s1)
        
    def shuffleTWO(self, no):
        #create a variable a deck of cards
        deck_cards = self.cards.items
        q1 = []
        s2 = []
        #remove the last card from the deck by no number and add to the Stack s1
        #each card that is draw or pop will be on the bottom of the deck
        for i in range(no):
            pop_q1 = deck_cards.pop()
            q1.insert(0, pop_q1)
        #remove the rest of the cards from the deck by length of the deck and add in Stack s2
        #each card that is draw or pop will be on the top of the s2 deck
        for i in range(len(deck_cards)):
            pop_s2 = deck_cards.pop()
            s2.append(pop_s2)
        while len(deck_cards) < 52:
            #if there are still cards in both q1 and s2, then put one by one into the deck
            if q1 != [] and s2 != []:
                pop_q1 = q1.pop()
                pop_s2 = s2.pop()
                self.cards.push(pop_q1)
                self.cards.push(pop_s2)
            #if cards in q1 is empty then add only cards from s2 back to the deck 
            if q1 == [] and s2 != []:
                pop_s2 = s2.pop()
                self.cards.push(pop_s2)
            #if cards in s2 is empty then add only cards from q1 back to the deck
            if s2 == [] and q1 != []:
                pop_q1 = q1.pop()
                self.cards.push(pop_q1)
    def shuffleTHREE(self, no):
        #create a variable a deck of cards
        deck_cards = self.cards.items
        q1 = []
        q2 = []
        #remove the rest of the cards from the deck by length of the deck and add in Stack q1
        #each card that is draw or pop will be on the top of the q1 deck
        for i in range(no):
            pop_q1 = deck_cards.pop()
            q1.insert(0, pop_q1)
        #remove the rest of the cards from the deck by length of the deck and add in Stack q2
        #each card that is draw or pop will be on the top of the q2 deck
        for i in range(len(deck_cards)):
            pop_q2 = deck_cards.pop()
            q2.insert(0, pop_q2)
        while len(deck_cards) < 52:
            #if there are still cards in both q1 and q2, then put one by one into the deck
            if q1 != [] and q2 != []:
                pop_q1 = q1.pop()
                pop_q2 = q2.pop()
                self.cards.push(pop_q1)
                self.cards.push(pop_q2)
            #if cards in q1 is empty then add only cards from q2 back to the deck 
            if q1 == [] and q2 != []:
                pop_q2 = q2.pop()
                self.cards.push(pop_q2)
            #if cards in q2 is empty then add only cards from q1 back to the deck
            if q2 == [] and q1 != []:
                pop_q1 = q1.pop()
                self.cards.push(pop_q1)

class Player:
    def __init__(self):
        self.cards = Stack()

    def points_eval(self):
        #create a list for calculate the total points
        points_list = []
        #create a variable total points
        total_points = 0
        #Make sure the value of ace is 11 to begin with
        ace_card_value = 11
        for i in range(len(self.cards.items)):
            points_list.append(self.cards.items[i])
        #sort list for easy calculation
        points_list.sort()

        #read every element in the list and add up all the point base on the card value to total points
        for i in range(len(points_list)):
            card = points_list[i]
            card_value = card[0]

            if card_value.isdigit():
                #check if adding the card value could exceed 21
                check_total_points = total_points + int(card_value)
                if check_total_points <= 21:
                    total_points = total_points + int(card_value)

            elif card_value == "T" or card_value == "J" or card_value == "Q" or card_value == "K":
                check_total_points = total_points + 10
                if check_total_points <= 21:
                    total_points = total_points + 10
            elif card_value == "A":
                ace_value_11 = total_points + 11
                ace_value_1 = total_points + 1
                #check if adding ace card to the total points could be greater than 21
                if ace_value_11 > 21:
                    #next ace card will have value of 1
                    ace_card_value = 1
                    total_points += ace_card_value
                elif len(points_list) >= 8 and ace_value_11 < 22:
                    ace_card_value = 1
                    total_points += ace_card_value
                else:
                    #if we have first ace in the hand and not greater than 21
                    total_points += ace_card_value
         #return the total ppoints                       
        return total_points

    def __str__(self):
        #print the string of cards in the deck
        return '{0}'.format(self.cards.items)

endgame = False
Gdeck = Deck()
Gdeck.shuffleTHREE(12)
P1 = Player()
P1.cards.push(Gdeck.cards.pop())
P1.cards.push(Gdeck.cards.pop())
print(P1)
print(P1.points_eval())
while (endgame == False):

    #input for the player if he want to draw another card
    user_input = input()
    if P1.points_eval() <= 21 and user_input == "y":
        #for the first turn of the player, he/she chooses to draw
        P1.cards.push(Gdeck.cards.pop())
        #asking if he/she wants one more card and showing the cards in their hands
        print("Do you want one more card? (y/n)", P1, sep="")
        #print the total points everytime after the drawing by calling point evaluation
        print(P1.points_eval())

        #check if the total point after the draw another card is greater than 21
        if P1.points_eval() > 21:
            #because he/she total point is greater than 21, then he/she loses the game
            print("GAME OVER!")
            #break to escape the while loop and save values
            break
    #if he/she doesn't want anymore cards ("n") and it is less than 21
    elif P1.points_eval() <= 21 and user_input == "n":
        print("Do you want one more card? (y/n)")
        #break to escape the while loop and save values
        break
