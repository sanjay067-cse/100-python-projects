import art
print("\n********************** WELCOME TO THE SECRET AUCTION **********************")
print(art.logo)    #printing logo from art.py

# function to compare all the bids when all the bids have been done
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner= bidder

    print(f"The Winner is {winner} with a bid of ${highest_bid}.")


bids = {}      #Empty dictionary to store names & bids of every person
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price        #Adding name and price of bid to the dictionary every time a new bidder joins
    should_continue = input("Are there any other bidders? Type 'yes or 'no'. \n")
    if should_continue == "no" :
        continue_bidding = False
        find_highest_bidder(bids)   #Function call to find out the highest bidder since no more further bids are to be done

    elif should_continue == "yes" :
        print("\n" * 50)            #Next bid will be done after a gap of 50 lines so that the next person is unable to see previous bids
