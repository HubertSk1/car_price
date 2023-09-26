import json
class car():
    def __init__(self,json_create:json,year):
        try:
            self.brand = json_create["itemOffered"]["name"].split(" ")[0]
            self.full_name = json_create["itemOffered"]["name"]
            self.fuel_type = json_create["itemOffered"]["fuelType"]
            self.price = {"currency":json_create["priceSpecification"]["priceCurrency"], "amount":int(json_create["priceSpecification"]["price"])}
            self.odometer = {"unit":json_create["itemOffered"]["mileageFromOdometer"]["unitCode"],"amount":json_create["itemOffered"]["mileageFromOdometer"]["value"]}
            self.model = json_create["itemOffered"]["name"].split(" ")[1]
            self.year= year
            if self.model == "seria":
                self.model +=" "+ json_create["itemOffered"]["name"].split(" ")[2]
            self.status = 0
        except:
            self.status = 1
    def __str__(self):
        if self.status == 0:
            return f"Car: {self.full_name}\nBrand: {self.brand}\nModel: {self.model}\nFuel Type: {self.fuel_type}\nPrice: {self.price['amount']} {self.price['currency']}\nOdometer: {self.odometer['amount']} {self.odometer['unit']}\nYear: {self.year}"
        else:
            return f"badly parsed"