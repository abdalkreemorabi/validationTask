from TransactionFactory import TransactionFactory

 
class TransactionValidator():

    def __init__(self, type,input):
        self.type = type
        self.input = input
        
        
    def validator(self):
        transactionFactory = TransactionFactory()
        source = transactionFactory.createInstance(self.type, self.input) 
        source.convertToObject()
        return source.validate()


test1=TransactionValidator("Xml","transaction.xml")
test1.validator()




