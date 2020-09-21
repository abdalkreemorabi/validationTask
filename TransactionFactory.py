from JsonData import JsonData
from XmlData import XmlData

 
def createInstance(source, input):
        sources = {"Json": JsonData(input), "Xml": XmlData(input)}
        return sources[source]

 
class TransactionFactory:

    def createInstance(self, source, input):
        createdInstance = createInstance(source, input)
        return createdInstance





