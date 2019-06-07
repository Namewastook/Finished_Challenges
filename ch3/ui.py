from menu import Outing, OutingRepo

x = 0

outings = []
total_cost = 0
golf_cost = 0
bowling_cost = 0
amusement_cost = 0
concert_cost = 0

orepo = OutingRepo()

while x == 0:
    print("Welcome to Komodo Outings\n")
    ui = input("What would you like to do today?\n"
               "1) Add an outing\n"
               "2) View all outings\n"
               "3) View costs of outings\n"
               "4) Exit\n"
               "> ")

    if ui == "1":
        total = 0

        outtype = input(
            "What type of outing are you adding?(golf, bowling, park, or concert)? ").lower()
        if orepo.valid_outing(outtype):
            pass
        else:
            print("Invalid outing type")
        attend = input("How many people went on the outing? ")
        date = input("When was the outing?(please use the format (mm/dd/yy)) ")
        costper = input("What was the cost per person? ")
        try:
            total = float(input(
                "What was the total cost of the event? Please use the format (dollars.cents)$"))
        except Exception:
            print("invalid cost.")
        total_cost += total
        if outtype == "golf":
            golf_cost += total
        elif outtype == "bowling":
            bowling_cost += total
        elif outtype == "park":
            amusement_cost += total
        elif outtype == "concert":
            concert_cost += total
        orepo.add_outing(outtype, attend, date, costper, total)
        print("Outting added!")
    elif ui == "2":
        tmp = orepo.get_outings()
        print("Type:    Ppl:    Date:      Cost per person:    Total Cost: \n")
        for outing in tmp:
            print(
                f"{outing.outtype}\t {outing.attend}\t {outing.date}\t {outing.costper}\t\t {outing.total}\t\n")
# thanks for the formatting help X!
    elif ui == "3":
        # orepo.view_costs()
        print(f"Total Cost: {total_cost}\n"
              f"Golfing Costs: {golf_cost}\n"
              f"Bowling Costs: {bowling_cost}\n"
              f"Park Costs: {amusement_cost}\n"
              f"Concert Costs: {concert_cost}\n")
        f = input("Press the enter/return key to go back to the main menu. \n"
                  " ")
    elif ui == "4":
        exit()
    else:
        print("Invalid input, please try again")


#code is buggy, but it works!#
