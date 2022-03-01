
# Import libraries and modules
from ParseTree import ParseTree
from Operator1 import Operator1
from Operator2 import Operator2
from Evaluate import Evaluate
import os

# Class to check for various errors
class ErrorCheck:
    def __init__(self, exp=None, inputFile=None, outputFile=None, imgFile=None, input3=None, float_input=None):
        self.exp=exp
        self.__input=inputFile
        self.__output=outputFile
        self.__img=imgFile
        self.input3=input3
        self.float_input = float_input

    # Getter function to get image file outside class
    def getImgFile(self):
        return self.__img
    
    # Seter function to set the image filename outside class
    def setImgFile(self,filename):
        self.__img=filename

    # Check if expression is fully parenthesized
    def checkParentheses(self,exp):
        exp_List=ParseTree(exp).splitExp()
        exp_copy=exp_List.copy()
        parenthesesCheck=True
        while parenthesesCheck==True and exp_copy!=['a']:
                inx=len(exp_copy)-exp_copy[::-1].index('(')-1   
                if exp_copy[inx+4]!=')':
                    parenthesesCheck=False
                else:
                    exp_copy[inx:inx+5]='a'
        return parenthesesCheck

    # Check if expressions are valid
    def checkExpression(self):
        success=False
        try:
            eval(self.exp)
            parenthesesCheck=self.checkParentheses(self.exp)
            if parenthesesCheck==True:
                success=True
            else:
                print('\nInvalid Expression! Please only enter FULLY parenthesized Math expression')  
        except:
            print('\nError! Please enter only valid FULLY parenthesised Math expression')
        return success

    # Check configuration file and adjust the settings accordingly
    def checkConfig(self):

        try:
            if open('config.txt', "r").read().splitlines()[1]=='1':
                evaluation = Operator1(self.exp).evaluate(ParseTree(self.exp).buildParseTree())
            elif open('config.txt', "r").read().splitlines()[1]=='2':
                evaluation = Operator2(self.exp).evaluate(ParseTree(self.exp).buildParseTree())
            else:
                print('\nOperator error! By default, program is set to operator 1')
                evaluation = Operator1(self.exp).evaluate(ParseTree(self.exp).buildParseTree())
        except:
            print('\nOperator error! By default, program is set to operator 1')
            evaluation = Operator1(self.exp).evaluate(ParseTree(self.exp).buildParseTree())
        return evaluation

    # Validate the input file given by user
    def checkInputFile(self):
        checkContent=False
        
        ## Check if file is text file
        if self.__input.endswith('.txt')==False:
            print('Invalid input file! Please ensure you have entered the appropriate TEXT filename.')

        ## Check if the file path exists
        elif os.path.exists(self.__input)==False:
            print('Input file does not exist!')
    
        ## Check if file is empty
        elif os.stat(self.__input).st_size==0:
            print('Input file is empty!')
        
        ## Checks if content in the file is valid math expressions
        elif checkContent==False:
            exps=Evaluate(self.__input).expList()
            for exp in exps:
                errorCnt=0
                try:
                    eval(exp)
                    parenthesesCheck=self.checkParentheses(exp)
                    if parenthesesCheck==True:
                        checkContent=True
                    else:
                        print('Please ensure all Math expressions in file are FULLY parenthesized') 
                except:
                    errorCnt=errorCnt+1
            if errorCnt>0:
                print('Error! Please ensure file only has valid Math expressions')
                
        return checkContent

    # Validate output file given by user
    def checkOutputFile(self):
        checkFile=False
        if self.__output.endswith('.txt')==False:
            print('Invalid output file! Please ensure you have entered the appropriate TEXT filename.')
        elif self.__output==self.__input:
            print('Error! Your output file is the same as input file')
        else:
            checkFile=True
        return checkFile

    # Validate image file given by user
    def checkImageFile(self):
        validFile=False
        ## Check if file only img file
        if self.__img.endswith('.png')==False and self.__img.endswith('.jpg')==False:
            print('Invalid image file! Please ensure you have entered either PNG or JPG filenames.')
        ## Check if the file path exists
        elif os.path.exists(self.__img)==True:
            print('Input file already exist!')
        else:
            validFile=True
        return validFile
    # Class to check if input is an integer for Option 5
    def int_input(self):
        try:
            number = int(self.input3)
            return True
        except ValueError as e:
            print("Not an integer! Try it again")
            return False
    # Class to check if input is a float for option 6
    def float_inputcheck(self):
        try:
            number = float(self.float_input)
            return True
        except ValueError as e:
            print("Not an Float! Try it again")
            return False

