# random for deal card function
import random
# function for dealing Card
def deal_card():
    card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    i = random.randint(0, len(card)-1)
    return card[i]
'''Check busted score if sum of score more than 21 check if they have A on hand return 11 to 1, if not return busted
'''
def check_busted(onhand):
    if sum(onhand) > 21:
        # check if 11 on hand and check sum of all after minus by 10 is more than 21, if not return busted 
        if 11 in onhand and sum(onhand) - 10 <= 21:
            # Message Change 11 to 1
            return "11 to 1"
        else:
            return "busted"
# Check win lose draw and Blackjack check : if they hold A and 10 card should be blackjack
def check_win(player,computer):
    if sum(player) > sum(computer):
        return "Player_win"
    elif sum(player) == sum(computer):
        return "Draw"
    else:
        return "Computer_win"
    
    if 11 in player[0:2] and 10 in player[0:2]:
        #blackjack player
        return "BJP"
    elif 11 in computer[0:2] and 10 in player[0:2]:
        #blackjack Computer
        return "BJC"
    elif 11 in player[0:2] and 10 in player[0:2] and 11 in computer[0:2] and 10 in player[0:2]:
        #blackjack Both
        return "BJB"

# deal card for player and computer with list comprehension
p1 = [deal_card() for i in range(2)]
c1 = [deal_card() for i in range(2)]  
# a for check if show somebody win
a = 0
# b is status for first black jack check
b = 0 

while True:
    print("P card is ",p1,"total score is ",sum(p1))
    print("C card is ",c1,"total score is ",sum(c1))
    
    # check blackjack in first draw
    if b == 0:
        if check_win(p1,c1) == "BJP":
            print("Player_win")
            break
        elif check_win(p1,c1) == "BJC":
            print("Computer_win")
            break
        elif check_win(p1,c1) == "BJB":
            print("Draw")
            break
        # status change
        b = 1 
    
    # prompt new card deal 
    ans = input('Would you like to draw another card?(yes/no)').lower()
    if ans == "yes":
        p1.append(deal_card())
    else:
        break
    print(p1)
    # new card deal for computer
    if sum(c1) <= 17:
        c1.append(deal_card())
    else:
        pass
    
    # Display card after deal
    print("P card after draw is ",p1,"total score is ",sum(p1))
    print("C card after draw is ",c1,"total score is ",sum(c1))
    print("")
    
    # check busted 
    if check_busted(p1) == "busted":
        print("Computer_win")
        a = 1
        break
    
    # check if A on hand change the value from 11 to 1
    elif check_busted(p1) == "11 to 1":
        for i in range(len(p1)):
            if p1[i] == 11:
                p1[i] = 1
    # same            
    if check_busted(c1) == "busted":
        print("Player_win")
        a = 1
        break
    elif check_busted(c1) == "11 to 1":
        for i in range(len(c1)):
            if c1[i] == 11:
                c1[i] = 1
    
# if a = 1 not come in   
if  a != 1:
    print(check_win(p1,c1))
