bidders = {}


def decide_winner(bids):
    highest_bid = 0
    highest_bidder = ""
    for key, value in bids.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidder = key
    print(f"The winners is {highest_bidder} with a bid of {highest_bid}$")


while True:
    bidder_name = input("What is your name?: ")
    bidder_amount = int(input("What's your bid?: "))

    bidders[bidder_name] = bidder_amount

    still_bidding = input("Are there any other bidders?: ")

    if still_bidding == "yes":
        continue
    else:
        decide_winner(bidders)
        break

