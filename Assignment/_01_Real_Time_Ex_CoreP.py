"""
problem:- workers monthly wages as per their daily work
"""
class DaysExceededError(Exception):
    pass

class CalculateWages:
    def __init__(self):
        self.no_of_workers = int(input("Enter total no. of workers:"))
        print("----------------------------------------")
        self.pay_perday = float(input("Enter per day work amount:"))
        print("----------------------------------------")
        self.dict_data = {}
        self.workerDB()
        self.showDB()

    def workerDB(self):
        total = 0
        while total < self.no_of_workers:
            name = input("Enter Name of worker:")
            total_wage = self.no_of_days()
            total += 1
            self.dict_data[name] = total_wage

    def no_of_days(self):
        try:
            no_day_wrk = float(input("Enter total no of days worked in a month:"))
            if no_day_wrk < 32:
                total_wage = self.pay_perday * no_day_wrk
                return total_wage
            else:
                raise DaysExceededError
        except DaysExceededError:
            print("Error :: Enter days available in a month < 32")
            return self.no_of_days()

    def showDB(self):
        print("----------------------------------------")
        print("Total Database",self.dict_data)



obj = CalculateWages()
