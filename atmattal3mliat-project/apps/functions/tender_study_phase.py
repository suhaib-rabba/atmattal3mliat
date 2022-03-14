import math


class Tender:
    def __init__(self, cost, period):
        self.cost = int(cost)
        self.period = int(period)

    def ald5ol(self):
        x = 0.01
        ald5ol_values = []
        for i in range(5):
            ald5ol_values.append(int(self.cost*x))
            x += .005
        return ald5ol_values

    def alta5ier(self):
        return math.ceil((self.cost*0.10)/(self.period*30))

    def minumumPayment(self):
        return math.ceil((self.cost*0.60)/self.period)
