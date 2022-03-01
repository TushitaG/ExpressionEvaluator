
# Evaluate class to read and store expressions from the user input file
class Evaluate:
    def __init__(self, inputFile=None):
        self.__input=inputFile # Input file entered by user is made into private variable
        self.answers=dict()

    # Function to read and return the contents of the input file   
    def readFile(self):
        file=open(self.__input, "r").read()
        return file
    
    # Split the math expressions by lines and store into list
    def expList(self):
        file=self.readFile()
        exp=file.replace('\n', ', ,').split(', ,')
        return exp
    
    # Getter function for input file to get it outside of this class
    def getInput(self):
        return self.__input
    
    # Setter function for input file to set a value for it outside of class
    def setInput(self,file):
        self.__input = file

    # Abstract class with no implementation
    def evaluate(self,tree):
        raise NotImplementedError("Subclass must implement abstract method")

