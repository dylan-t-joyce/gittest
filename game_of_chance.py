def coin_flip(bet,guess):
    num = random.randint(1, 2)
    if num == 1 and guess == "Tails":
        outcome = "Won"
        winnings = bet *2
    if num == 2 and guess == "Heads":
        outcome = "Won" 
        winnings = bet * 2
    else: 
        outcome = "Lost"
        winnings = 0
    return winnings - bet

money += coin_flip(10,"Heads")    
print (money)
money += coin_flip(10,"Heads")    
print (money)
money += coin_flip(10,"Heads")    
print (money)