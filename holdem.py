# coding=utf-8
import random

deck = [
['H',2],['H',3],['H',4],['H',5],['H',6],['H',7],['H',8],['H',9],['H',10],['H',11],['H',12],['H',13],['H',14],
['D',2],['D',3],['D',4],['D',5],['D',6],['D',7],['D',8],['D',9],['D',10],['D',11],['D',12],['D',13],['D',14],
['C',2],['C',3],['C',4],['C',5],['C',6],['C',7],['C',8],['C',9],['C',10],['C',11],['C',12],['C',13],['C',14],
['S',2],['S',3],['S',4],['S',5],['S',6],['S',7],['S',8],['S',9],['S',10],['S',11],['S',12],['S',13],['S',14]
]

def shuffle():  #Randomly selects cards from deck and appends them to a new shuffled deck
    global deck
    resetdeck()
    shuffledDeck = []
    while len(deck) > 0:
        index = random.randint(0, len(deck) - 1)
        shuffledDeck.append(deck[index])
        deck.pop(index)
    deck = shuffledDeck
def resetdeck():        #reset the deck at the end of a round because there are discarded cards
    global deck
    reset = [
    ['H',2],['H',3],['H',4],['H',5],['H',6],['H',7],['H',8],['H',9],['H',10],['H',11],['H',12],['H',13],['H',14],
    ['D',2],['D',3],['D',4],['D',5],['D',6],['D',7],['D',8],['D',9],['D',10],['D',11],['D',12],['D',13],['D',14],
    ['C',2],['C',3],['C',4],['C',5],['C',6],['C',7],['C',8],['C',9],['C',10],['C',11],['C',12],['C',13],['C',14],
    ['S',2],['S',3],['S',4],['S',5],['S',6],['S',7],['S',8],['S',9],['S',10],['S',11],['S',12],['S',13],['S',14]
    ]
    deck = reset[:]
    
def deal():     #deal the top two cards to one player
    global deck
    hand = []
    hand.append(deck.pop(0))
    hand.append(deck.pop(0))
    return hand

def dealrigged(cards):      #used for testing, deals wanted cards
    global deck
    hand = []
    while len(cards) > 0:
        for i in range(len(deck)):
            if deck[i] == cards[0]:
                hand.append(deck[i])
                deck.pop(i)
                cards.pop(0)
                break
    return hand
    
def display(cards):         #Used to print the cards onto the screen in rows, therefore need to print 1 line at a time
    conversion = {'H':'♥','S':'♠', 'D':'♦','C':'♣', 1:' 1', 2:' 2', 3:' 3', 4:' 4', 5:' 5', 6:' 6', 7:' 7', 8:' 8', 9:' 9', 10:'10', 11:' J', 12:' Q', 13: ' K', 14:' A'}
    for i in range(len(cards)):
        print("┌───────┐", end = " ")
    print("")
    for i in range(len(cards)):
        convNum = conversion[cards[i][1]]
        print("│" + str(convNum) + "     │", end = " ")
    print("")
    for i in range(len(cards)):
        print("│       │", end = " ")
    print("")
    for i in range(len(cards)):
        convSuit= conversion[cards[i][0]]
        print("│   " + str(convSuit) + "   │", end = " ")
    print("")
    for i in range(len(cards)):
        print("│       │", end = " ")
    print("")
    for i in range(len(cards)):
        convNum = conversion[cards[i][1]]
        print("│    " + str(convNum) + " │", end = " ")
    print("")
    for i in range(len(cards)):
        print("└───────┘", end = " ")
    print("")        
    return

def getHandValue(playerHand, table):        #This func determines hand values, giving each hand a unique score
    handMultiplier = {      #Combo multipliers to move hand scores into their own distinct catagory
    "HighCard": 0, 
    "Pair":2000, 
    "TwoPair":3000, 
    "Triple":4000, 
    "Straight":5000, 
    "Flush":6000, 
    "FullHouse":7000, 
    "Quads":8000, 
    "StraightFlush":9000, 
    "RoyalFlush": 10000
    }
    cardValue = {       #f(x) = 18.8((1.1**x)x)
    2:46,               #These are used similarly but for kickers and HighCard combos    
    3:75,
    4:110,
    5:151,
    6:200,
    7:256,
    8:322,
    9:399,
    10:488,
    11:590,
    12:708,
    13:844,
    14:999
    }
    hand = []
    kicker = 0
    hand.append(playerHand[0])
    hand.append(playerHand[1])
    for card in table:          #Create a list of all cards in hand and in table
        hand.append(card)
    
    values = {}
    suits = {}
    numbers = []
    
    for card in hand:               #This loop records frequencies that each value/suit appear
        if card[1] not in values:
            values[card[1]] = 1
            numbers.append(card[1])
        else:
            values[card[1]] += 1

        if card[0] not in suits:
            suits[card[0]] = 1
        else:
            suits[card[0]] += 1        

    pair = False
    triple = False
    quads = False
    flush = False
    fullhouse = False
    straight = False
    score = 0
    playCard = 0
    playCard2 = 0
    needKicker = False
    straightCard = 0
    flushCard = 0
    straightflush = False
    royalflush = False
    pairCards = []
    highCard = 0
    twopair = False
    
    
    for num in values:          #Search dictionary for pairs, triples, or quads
        if values[num] == 2:
            pair = True
            pairCards.append(num)
        if values[num] == 3:
            triple = True
            tripleCard = num
        if values[num] == 4:
            quads = True
            quadCard = num
        if pair == True and triple == True:
            fullhouse = True
    
    for card in playerHand:     #Find the highcard out of the two cards the player has in hand (index 1 is for numbers)
        if card[1] > highCard:
            highCard = card[1]
      
        
    
    if len(pairCards) > 1:          #Determines the two highest pairs in case the hand has 3 pairs
        largestPair = 0
        secondlargestPair = 0
        for card in pairCards:
            if card > largestPair:
                secondlargestPair = largestPair
                largestPair = card
        twopair = True
        twopairCard1 = largestPair
        twopairCard2 = secondlargestPair
    
    for suit in suits:          #Check for flush (5 of one suit)
        if suits[suit] == 5:
            flush = True
            flushSuit = suit
            highest = 0
            flushCards = []
            for card in hand:
                if card[0] == flushSuit:
                    flushCards.append(card[1])
                    if card[1] > highest:
                        highest = card[1]
            flushCard = highest
            
    numbers = bubblesort(numbers)       #sort the numbers list lowest to highest
    sequence = []
    for i in range(len(numbers) - 4):       #To check for straights, the loop looks at blocks of 5 cards at a time. If the difference between them is 4 they are sequential. Extra case for ace low straight
        if numbers[i+ 4] - numbers[i] == -9 and numbers[0] == 14:
            sequence = numbers[i:i+5]
        if numbers[i+ 4] - numbers[i] == 4:
            sequence = numbers[i:i+5]
            

    if len(sequence) == 5:      #If there is a straight, it will be defined by the highest card in that straight
        straight = True
        straightCard = sequence[len(sequence)-1]

    
    if (straight and flush) == True and straightCard == flushCard and straightCard == 14:       #If there is a straight, flush, and the highcard is an ace, the hand is a royal flush
        royalflush = True
        royalflushCard = straightCard 
    elif (straight and flush) == True and straightCard == flushCard:        #If there is a flush and a straight, hand is a straight flush
        straightflush = True
        straightflushCard = straightCard
        
    
    #---------------------------------------
    #Check hand combinations in order from most relevant to least relevant
    if royalflush == True:
        playCard = royalflushCard
        combo = "RoyalFlush"
    elif straightflush == True:
        playCard = straightflushCard
        combo = "StraightFlush"
    elif quads == True:
        playCard = quadCard
        combo = "Quads"
    elif fullhouse == True: #FullHouse
        combo = "FullHouse"
        playCard = tripleCard   
    elif flush == True:
        combo = "Flush"
        playCard = flushCard
    elif straight == True:
        playCard = straightCard
        combo = "Straight"
    elif triple == True:
        playCard = tripleCard
        combo = "Triple"
        needKicker = True
    elif twopair == True:   
        playCard = twopairCard1
        playCard2 = twopairCard2
        combo = "TwoPair"
        needKicker = True
    elif pair == True:      #Pair
        playCard = pairCards[0]
        combo = "Pair"
        needKicker = True
    else:
        playCard = highCard
        combo = "HighCard"
        needKicker = True

    for card in playerHand:     #Find Kicker (highest card in hand that isn't in a combo)
        if card[1] != (playCard or playCard2) and card[1] > kicker and needKicker == True:
            kicker = card[1]
            
    score = handMultiplier[combo] + cardValue[playCard] + kicker        #Multiply the playCard (card that defines the combo) by the combo multiplier plus the kicker if needed
    return score, combo
    
def bubblesort(alist):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1, len(alist)):
            if int(alist[i-1]) > int(alist[i]):
                alist[i-1] ,alist[i] = alist[i], alist[i-1]
                swapped = True
    if 14 in alist:
        alist.insert(0, 14)
    return alist    

def bet(playerPot,oppPot, chips, oppchips):   #Menu for player's betting choices
    global pot
    global roundnum
    bet = 0
    choice = ""
    print("┌─────────┐\n│ OPTIONS │\n└─────────┘\n 1. call\n 2. raise\n 3. fold ")
    while choice != ('1' or '2' or '3'):
        choice = input()
        if choice == '1':
            playerPot = call(playerPot, chips)
            break
                
        if choice == '2':
            if roundnum == 1 and (pot == 0 or 100 > pot > 0):       #If the player attempts to raise before calling the blind
                print("You must call the blind")
                continue
            result = raisebet(playerPot, oppPot, chips, oppchips)
            if result == -1:
                choice == ""
                continue
            playerPot = result
            break
        if choice == '3' and pot == 0 and roundnum == 1:
            print("You must atleast call the Small Blind")
            choice = 0
        elif choice == '3' and 100 > pot > 0 and roundnum == 1:
            print("You must atleast call the Big Blind")
            choice = 0
        elif choice == '3':
            playerPot = fold()
            break
            
    return playerPot
def fold():         #-1 is the "folded" flag
    playerPot = -1
    return playerPot
    
def raisebet(playerPot,oppPot, chips, oppchips, amount = 0):     #Raise function that allows user to bet a specific amount
    global roundnum, pot, minraise
    
    if roundnum == 1:
        minraise = 100
    while (amount < minraise) or (amount > chips) or (amount > oppchips + oppPot - playerPot):      #Loop through if the amount is invalid
        if amount == 0:
            amount = int(input("amount (-1 to go back): "))
        if amount < minraise and amount != oppchips and amount != chips and amount != -1:
            print("Min-raise: " + str(minraise))
            amount = 0
        elif amount > chips:               #Automated all in if user enters a higher value than their stack
            amount = chips
            print("ALL-IN for $" + str(amount))
            break;
        elif amount > oppchips + oppPot - playerPot:            #Automatically adjusts bet to be equal to opponents all in
            amount = oppchips + oppPot - playerPot
            print("You have put opponent all-in for $" + str(amount))
            break
        if amount == -1:        #return to menu
            return -1
    pot += amount
    playerPot += amount
    bet = amount
    minraise = 2*bet
    print("RAISE $" + str(bet))
    return playerPot

def call(playerPot, chips):     #Match the opponents bet
    global roundnum, pot
    
    smallBlind = 50
    bigBlind = 100
    if pot == 0:        #Put the small blind in if its the first round, otherwise a call at 0 is a check
        bet = smallBlind  
        if chips < smallBlind:
            bet = chips
        if roundnum > 1:        #This is the check scenario
            bet = 0
            print("CHECK")
            return 0
    elif pot < bigBlind and roundnum == 1:          #Put the big blind in at round 1
        bet = bigBlind
        if chips < bigBlind:
            bet = chips
    else:
        bet = pot - 2*playerPot        
    pot += bet
    playerPot += bet
    
    
    print("CALL $" + str(bet))
    return playerPot

 



def roundHandle(playerTurn, buffyHand, playerHand, table):              #Round loop, finishes once the round has been fulfilled
    global roundnum, pot, totalPot, playerChips, buffyChips,minraise

    playerPot = 0
    buffyPot = 0
    pot = 0
    roundnum += 1
    counter = 0
    playermove = 0
    lastmove = 0
    minraise = 1
    
    
    if playerTurn == "SMALL":           #Which player starts
        currentMove = "Player"
        
    else:
        currentMove = "Buffy"
    
    while True:
        if (buffyChips == 0 or playerChips == 0) and (playerPot == buffyPot or (pot > 100 and pot <= 150)):   #If these parameters are true, the round is over     
            totalPot = totalPot + playerPot + buffyPot
            return
        if currentMove == "Player":
            if playerPot != buffyPot or counter < 2:
                print("\n" + str(currentMove) + "\nPot:   $" + str(pot) + "\nShare: $" + str(playerPot) + "\nChips: $" + str(playerChips))
                ogPot = playerPot
                playermove = bet(playerPot, buffyPot, playerChips, buffyChips)
                playerPot = playermove      #Record the change in player's pot this round
                if playerPot != -1:
                    playerChips = playerChips - (playerPot - ogPot)
                lastmove = playermove - ogPot           #records the player's last move so buffy can see it
                currentMove = "Buffy"
                
        
        elif currentMove == "Buffy":
            if playerPot != buffyPot or counter < 2:
                print("\n" + currentMove, "\nPot:   $" + str(pot) + "\nShare: $" + str(buffyPot) + "\nChips: $" + str(buffyChips), "\n")
                ogPot = buffyPot
                move = buffyBrain(buffyPot,playerPot, lastmove, buffyHand, playerHand, playerTurn, playerChips, table)
                buffyPot = move
                if buffyPot != -1:
                    buffyChips = buffyChips - (buffyPot - ogPot)
                currentMove = "Player"
        
        counter += 1
        if playerPot == -1:
            print("PLAYER folds")
            totalPot += pot
            win("buffy")
            return "fold"
        if buffyPot == -1:      #A fold immediately quits the round and the winner is the opposite player
            print("BUFFY folds,")
            totalPot += pot
            win("player")
            return "fold"
        if playerPot == buffyPot and counter > 2:  #The counter is used for cases where the first player checks. Since this is equal to a bet of 0 the pots will technically be equal and the round would end
            totalPot += pot
            return

def updateTable(table):     #Func called at the end of each round to update the table cards and progress to next round. Flop -> add 3 cards to table, etc.
    global deck, roundnum
    if roundnum == 1:  #Flop
        input("Here comes the flop...\n")
        table.append(deck.pop(0))
        table.append(deck.pop(0))
        table.append(deck.pop(0))
    if roundnum == 2:  #Turn
        input("Next is the turn...\n")
        table.append(deck.pop(0))
    if roundnum == 3:  #River
        input("Here's the river...\n")
        table.append(deck.pop(0))
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("_________________________________________________")
    print("                      Table                      ")
    display(table)
    print("_________________________________________________")
    print("                   Your hand:")
    return table
    
def win(winner):       #Func thats called when someone wins a round, they are transfered the totalpot to their stack
    global playerChips, buffyChips, totalPot
    if winner == "player":
        input("\nPLAYER wins $" + str(totalPot) + "\n")
        playerChips += totalPot
    if winner == "buffy":
        input("\nBUFFY wins $" + str(totalPot) + "\n")
        buffyChips += totalPot
    if winner == "tie":
        input("\nCHOPPED POT\n")
        buffyChips += totalPot/2
        playerChips += totalPot/2
    totalPot = 0
        

def showdown(playerHand, buffyHand, table):         #If a bet on the river is called, it procceeds to showdown. Both players show their cards
    playerValue = getHandValue(playerHand, table)    #Calculate hand scores for each player   
    buffyValue = getHandValue(buffyHand, table)
    playerScore = playerValue[0]
    buffyScore = buffyValue[0]
    playerCombo = playerValue[1]
    buffyCombo = buffyValue[1]
    input("\nSHOWDOWN\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("_________________________________________________")
    print("                   Final Table                   ")
    display(table)
    print("_________________________________________________")
    print("                You have:", playerCombo)
    display(playerHand)
    print("_________________________________________________")
    print("                Buffy has:", buffyCombo)
    display(buffyHand)
    print("_________________________________________________")
    if playerScore > buffyScore:            #Compare hand scores and determine winner
        win("player")
    if buffyScore > playerScore:
        win("buffy")
    if playerScore == buffyScore:
        win("tie")
    return

def game(playerTurn, buffyTurn):        #Game loop
    global pot, totalPot, roundnum
    table = []
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    input("Shuffling deck...")
    print(roundnum)
    pot = 0
    playerPot = 0
    buffyPot = 0
    shuffle()
    playerHand = deal()
    buffyHand = deal()
    #playerHand = dealrigged([['C', 13],['C',6]])
    #buffyHand = dealrigged([['C', 10],['S',10]])
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("You are " + playerTurn + " BLIND.")
    print("Your hand is:")
    
    display(playerHand)
    result = roundHandle(playerTurn, buffyHand, playerHand, table)
    while result != "fold" and roundnum < 4:    #This loops through all until someone folds or the game procceeds to showdown  
        print("The pot is: $" + str(totalPot))
        updateTable(table)
        display(playerHand)
        print("_________________________________________________")
        result = roundHandle(playerTurn, buffyHand, playerHand, table)
        if result == "fold":
            return
    if result != "fold":
        showdown(playerHand, buffyHand, table)
    return
def gameover():
    print("GAMEOVER")
    
def buffyBrain(buffyPot,playerPot, playermove, buffyHand, playerHand,playerTurn, playerChips, table):  #This is called instead of the bet() function for Buffy to make a decision
    global pot, roundnum, deck, buffyChips, totalPot
    
    equity = montecarlo(buffyHand, playerHand, table)
    loss_percentage = 1 - equity
    EV = (equity*(totalPot + pot)) - (loss_percentage * playermove) #Estimated value. This is the average profit to be made in the long run if the bet is called
    
    raised = False
    if playermove > 100:            #flag to tell Buffy when he has been raised
        raised = True
        
    variation = random.randint(1,4)     #random variation for betsizes to reduce predictability
    
    if roundnum == 1 and (playermove == 0 or playermove == 50):           #Buffy will always call the blind
        buffyPot = call(buffyPot, buffyChips) 
        return buffyPot
    if playerChips == 0 or (playermove + playerPot == buffyChips + buffyPot):             #player moves all in or forces you all in
        if roundnum ==4:        #Decision making if its the river
            if equity > .70:
                buffyPot = call(buffyPot, buffyChips)
            else:
                buffyPot = fold()
        else:
            if equity > .60:
                buffyPot = call(buffyPot, buffyChips)
            else:   
                buffyPot = fold()
    elif equity > .50:          #If buffy has a positive winrate hand
        if raised == True:
            if EV > -10:
                buffyPot = raisebet(buffyPot, playerPot, buffyChips, playerChips, playermove*2)
            elif EV > 50:
                buffyPot = call(buffyPot, buffyChips)
            else:
                buffyPot = fold()
        elif equity > 80 and roundnum == 4:
            buffyPot = raisebet(buffyPot,playerPot, buffyChips, playerChips, buffyChips)
        elif equity > .70:
            buffyPot = raisebet(buffyPot, playerPot, buffyChips, playerChips, (betsizer(playerChips*.1)*variation))
        elif equity > .60:
            buffyPot = raisebet(buffyPot,playerPot, buffyChips, playerChips, betsizer(playerChips*.05)*variation)
        else:
            buffyPot = call(buffyPot, buffyChips)
    elif equity <= .50:      #If Buffy has a below 50 winrate hand
        if playermove == 0 and random.randint(1,3) == 3:
            buffyPot = raisebet(buffyPot,playerPot, buffyChips, playerChips, betsizer(playerChips*.05)*variation)  #bluff
        elif EV >= 10:
           buffyPot = call(buffyPot, buffyChips)
        elif EV < 10:
            buffyPot = fold()      
            
               
    return buffyPot
    
def betsizer(num):      #Func for creating even bet sizes
    counter = 0
    chipsize = 50
    while num > 0:
        num -= chipsize
        counter += 1
    return counter * chipsize
    
def montecarlo(buffyHand, playerHand, original_table):      #MonteCarlo simulation used to determine Buffy's equity against any random hand and any random table progression
    global deck
    newdeck = deck[:]
    newdeck.insert(random.randint(0,len(newdeck) - 1),playerHand[0])        #Insert the player's cards back into the deck becuase Buffy doesnt know them
    newdeck.insert(random.randint(0,len(newdeck) - 1),playerHand[1])
    win = 0
    lose = 0
    tie = 0
    n = 300         #n is the number of hands and the number of random draws the loop will test. For each n random hands n random table draws are compared
    
    for i in range(n):
        oppHand = []
        while len(oppHand) < 2:
            randCard = random.randint(0,len(newdeck)-1)
            if newdeck[randCard] not in oppHand:
                oppHand.append(newdeck[randCard])
        for i in range(n):
            newtable = original_table[:]
            while len(newtable) < 5:
                randomDraw = random.randint(0,len(newdeck)-1)
                if newdeck[randomDraw] not in (newtable and oppHand):
                    newtable.append(newdeck[randomDraw])
            playerScore = getHandValue(oppHand, newtable)[0]
            buffyScore = getHandValue(buffyHand, newtable)[0]
            #print(playerScore,buffyScore)
            if playerScore > buffyScore:
                lose += 1
            elif buffyScore > playerScore:
                win += 1
            elif buffyScore == playerScore:
                tie += 1
    equity = (win+tie) / (win+lose+tie)  #Divide the wins/ties over the games simulated 
    return equity
    
roundnum = 0
totalPot = 0
playerChips = 5000
buffyChips = 5000

coin = random.randint(1,2)      #Flip a coin to determine who starts
if coin == 1:
    playerTurn = "BIG"
    buffyTurn = "SMALL"
else:
    playerTurn = "SMALL"
    buffyTurn = "BIG"

while True:
    game(playerTurn,buffyTurn)  #once this is done the game is over (those
    if buffyChips == 0 or playerChips == 0:     # if either one of the players is out of chips the game is over.
        gameover()
        
        break           
    roundnum = 0
    playerTurn, buffyTurn = buffyTurn, playerTurn       #Players switch turns

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    