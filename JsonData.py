import json
import math


class JsonData:

    def __init__(self, input):
        self.input = input
        self.data = ''
    
    def convertToObject(self):
        try:
            with open(self.input) as json_data:
                self.data = json.load(json_data)
                return self.data
        except:
            print("File " + self.input + " not found")
            return 
        
    def validate(self):
        try:
            taxRate = self.data["taxes"][0]["rate"]
            priceWithTax = self.data["total_collected_money"]["amount"]
            netSale = self.data["itemization"][0]["gross_sales_money"]["amount"]
             
            netSaleCalculated  = int(priceWithTax / (taxRate+1))
            print("The tax rate retrieved from Json file =" , taxRate)
            print("The total price retrieved from Json file =" , priceWithTax)
            print("The net sale retrieved from Json file =" , netSale)
            print("The net sale calculated from this program =" , netSaleCalculated) 
            if (netSaleCalculated) != (netSale):
                return print("The net sale calculated is /NOT\ equal to the net sale retrieved from Json file")     

        except:
             print("Invalid data type")
             return False
      
        return print("The net sale calculated is equal to the net sale retrieved from Json file")


