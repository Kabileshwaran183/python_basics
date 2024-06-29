from replit import clear
from art_bidding import logo
print(logo)
bids = {}
def bid_result(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bid_continue=True
while bid_continue:
    name=input("What is your name:")
    price= int(input("bid: $"))
    bids[name]=price
    should_continue=input('"yes" or "no"').lower()
    if should_continue == "no" :
        bid_continue=False
        clear()
        bid_result(bids)
    elif should_continue == "yes" :
        clear()
