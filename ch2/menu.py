import datetime


class Claim:
    def __init__(self, claimid, claimtype, desc, amount, incidentdate, claimdate, isvalid):
        self.claimid = claimid
        self.claimtype = claimtype
        self.desc = desc
        self.amount = amount
        self.incidentdate = incidentdate
        self.claimdate = claimdate
        self.isvalid = isvalid

    def __repr__(self):
        return f"Claim ID: {self.claimid} \n Claim Type: {self.claimtype} \n Description: {self.desc}\n Claim Amount: {self.amount}\n Incident Date: {self.incidentdate}\n Claim Date: {self.claimdate}\n Is Valid? {self.isvalid}\n"


class ClaimRepo:
    def __init__(self):
        self.claims_list = []

    def make_claim(self, claimid, clametype, desc, amount, incidentdate, claimdate, isvalid):
        new_claim = Claim(claimid, clametype, desc, amount,
                          incidentdate, claimdate, isvalid)
        self.claims_list.append(new_claim)
        return True

    def get_list(self):
        return self.claims_list

    def del_claim(self, claimid):
        for claim in self.claims_list:
            if claimid == claim.claimid:
                self.claims_list.remove(claim)
                return True


# print(ClaimRepo.get_list)
# ClaimRepo.make_claim(1, "auto", "things happend", 100, "today", "today", True):
# print(ClaimRepo.get_list)
