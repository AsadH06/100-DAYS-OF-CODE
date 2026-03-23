import os

def auction():

    biddings = {}

    bidding = True
    while bidding:
        name = input("What is your name: ")
        bid = int(input("What is your bid price: "))
        biddings[name] = bid
        bidding_continue = input("Is there anyone else who want to bid as well? 'y' for yes and 'n' for no ").lower()

        if bidding_continue == "y":
            os.system('cls')

        else:
            # highest_bid = 0
            # bidder_name = ''
            # for key,value in biddings.items():
            #     if value > highest_bid:
            #         highest_bid = value
            #         bidder_name = key
            # print(f"The highest bid is ${ highest_bid}. \nIt is from {bidder_name}")

            highest_bid = max(biddings, key = biddings.get)
            print(f"The winner is {highest_bid} with the bid of ${biddings[highest_bid]}")


            bidding = False

auction()






