from JsonData import JsonData
from XmlData import XmlData

 
def createInstance(source, input):
    try:
        sources = {"Json": JsonData(input), "Xml": XmlData(input)}
        return sources[source]
    except:
        print(source + " Data not supported, we are supporting json and xml")
        return False


 
class TransactionFactory:

    def createInstance(self, source, input):
        createdInstance = createInstance(source, input)
        return createdInstance





