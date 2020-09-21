from xml.etree.ElementTree import parse
import math


class XmlData:

    def __init__(self, input):
        self.input = input
        self.data = ''
    
    def convertToObject(self):
        try:
            self.data = parse(self.input)
            return self.data
        except:
            print("File " + self.input + " not found")
            return
    
    def validate(self):

        try:
            findNetSale = self.data.find('./itemization/element/gross_sales_money/amount')
            netSale = findNetSale.text

            findTaxRate = self.data.find("./itemization/element/taxes/element/rate")
            taxRate = findTaxRate.text

            findPriceWithTax = self.data.find("./itemization/element/total_money/amount")
            priceWithTax = findPriceWithTax.text

            netSaleCalculated = int(int(priceWithTax) / (float(taxRate) + 1))
            print("The tax rate retrieved from Json file =" , taxRate)
            print("The total price retrieved from Json file =" , priceWithTax)
            print("The net sale retrieved from Json file =" , netSale)
            print("The net sale calculated from this program =" , netSaleCalculated)     
            if netSaleCalculated != int(netSale):
                return print("The net sale calculated is /NOT\ equal to the net sale retrieved from XML file")

        except:
            print("Invalid data type")
            return False
        
        return print("The net sale calculated is equal to the net sale retrieved from XML file")


