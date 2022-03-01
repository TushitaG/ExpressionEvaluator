# Name: Jumana Haseen
# StudentID: 2021627
# Class: DAAA/FT/2B/02

# Report class to print the expression evaluation report
class Report:

    def __init__(self, values, answers, outputFile):
        self.values=values
        self.answers=list(enumerate(answers.items()))
        self.__output=outputFile
        self.uniqueVal=list(set(list(values)))
        
    # Getter function to get output file outside class
    def getOutputFile(self):
        return self.__output
    
    # Seter function to set the output filename outside class
    def setOutputFile(self,filename):
        self.__output=filename
    
    # Prints the whole analysis report into the output file
    def reportFile(self):
        file=open(self.__output, "w")
        for i in range(len(self.uniqueVal)):
            print(f'\n*** Expressions with value = {self.uniqueVal[i]}',file=file)
            for j in range(len(self.answers)):   
                if self.answers[j][1][1]==self.uniqueVal[i]:
                    print(f"{self.answers[j][1][0].replace(' ','')} ==> {self.uniqueVal[i]}",file=file)
        file.close()

    # The printed output in the output file is read and displayed into the screen   
    def readReport(self):
        self.reportFile()
        f=open(self.__output,"r")
        return '\n>>> Evaluation and sorting started:\n'+f.read()+'\n>>> Evaluation and sorting completed!'
        