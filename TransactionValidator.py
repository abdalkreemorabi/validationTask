from TransactionFactory import TransactionFactory

 
class TransactionValidator():

    def __init__(self, type,input):
        self.type = type
        self.input = input
        
        
    def validator(self):
        transactionFactory = TransactionFactory()
        source = transactionFactory.createInstance(self.type, self.input)
        while(source):
          source.convertToObject()
          return source.validate()






