from menu import *
import datetime

x = 0
cr = ClaimRepo()

while x == 0:
    print("\n")
    user_input = input("Komodo Claims Department \n"
                       "What would you like to do? \n"
                       "1) Make a new claim: \n"
                       "2) View all claims: \n"
                       "3) Take care of a claim: \n"
                       "4) Exit: \n"
                       "> ")
    print("\n")
    if user_input == "1":
        claimid = input("Claim id number: ")
        clmtype = input("Type of claim (Car, Home, or Theft): ")
        desc = input("Enter a brief description of the incident: ")
        amount = input("How much is the claim for?: ")

        incidentdate1 = int(input("Day of the incident (dd): "))
        incidentdate2 = int(input("Month of the incident (mm): "))
        incidentdate3 = int(input("Year of the incident (yyyy): "))
        incidentdate = datetime.date(
            year=incidentdate3, month=incidentdate2, day=incidentdate1)

        claimdate1 = int(input("Day the claim was filed (dd): "))
        claimdate2 = int(input("Month the claim was filed (mm): "))
        claimdate3 = int(input("Year the claim was filed (yyyy): "))
        claimdate = datetime.date(
            year=claimdate3, month=claimdate2, day=claimdate1)

        diff = claimdate - incidentdate
        diff = str(diff).split(" ")
        if int(diff[0]) <= 30:  # This is hacky, but it works, the claim cannot be filed on the same day of the incident though, this can be fixed later. Just trying to get it to work
            isvalid = True
            print("The claim is valid, will be filed and paid out accordingly")
        else:
            isvalid = False
            print(
                "The claim is more then 30 days old, is not valid, and will not be paid out.")

        resp = cr.make_claim(claimid, clmtype, desc, amount,
                             incidentdate, claimdate, isvalid)
        if resp:
            print("Claim added!")

    elif user_input == "2":
        claim_list = cr.get_list()
        for claim in claim_list:
            print(claim)

    elif user_input == "3":
        print("Here is the next claim to be taken care of: \n"
              "Claim ID: \nClaim Type: \nDescription: \nClaim Amount: \nIncident Date: \nClaim Date: \nClaim Valid: ")
        try:
            temp = cr.claims_list[0]
            print(temp)
            yes_or_no = input(
                "Do you want to take care of this claim now? (yes/no): ").lower()
            if yes_or_no == "yes":
                cr.del_claim(temp.claimid)
                print("The claim has been taken care of.")
            elif yes_or_no == "no":
                pass
            else:
                print("Invalid input, please make a selection from those provided.")

        except Exception:
            print("There are no claims currently available.")
            pass
    elif user_input == "4":
        exit()
    else:
        print("Invalid input, please make a selection from the numbers provided.")
        pass


# clean coding, the pragmatic programmer, cracking the coding interview, design patterns, data structures and algorithms. Books to look at!
