outings = []
total_cost = 0
golf_cost = 0
bowling_cost = 0
amusement_cost = 0
concert_cost = 0


class OutingRepo:
    def valid_outing(self, type_outing):
        valid = ["golf", "bowling", "park", "concert"]
        if type_outing in valid:
            return True
        else:
            return False

    def add_outing(self, outtype, attend, date, costper, total):
        outings.append(Outing(outtype, attend, date, costper, total))

    def get_outings(self):
        return outings

    # def view_costs(self):
    #     print(f"Total Cost: {total_cost}\n"
    #           f"Golfing Costs: {golf_cost}\n"
    #           f"Bowling Costs: {bowling_cost}\n"
    #           f"Amusement Park Costs: {amusement_cost}\n"
    #           f"Concert Costs: {concert_cost}\n")
    #     return total_cost

    # moved into ui.py


class Outing:
    def __init__(self, outtype, attend, date, costper, total):
        self.outtype = outtype
        self.attend = attend
        self.date = date
        self.costper = costper
        self.total = total

    def __repr__(self):
        return f"{self.outtype}\n{self.attend}\n{self.date}\n{self.costper}\n{self.total}"
