
# MAIN PROGRAM OF APPLICATION

# import all necessary classes
import random
from Evaluate import Evaluate
from SortExpressions import SortExpressions
from Report import Report
from ParseTree import ParseTree
from ErrorCheck import ErrorCheck
from VerticalTree import VerticalTree
from ConstructTree import ConstructTree
from DrawTree import DrawTree
from Expression import Expression
from HashTable import HashTable
from SweetMath import SweetMath
from BST import BST
from printMode import Vertical
from drawGraph import GraphTurtle

# Print the header with the name, id and class
print('\n**********************************************************************')
print('* ST1507 DSAA: Expression Evaluator & Sorter                         *')
print('*--------------------------------------------------------------------*')
print('*                                                                    *')
print('*  - Done by: Jumana Haseen (2021627) & Tushita Govindaraj (xxxxxxx) *')
print('*  - Class: DAAA/2B/02                                               *')
print('**********************************************************************')

response=''
order = 'i'
pmode = 'h'
treeDiag='n'

while response!='7':
    expError=False
    inputContent=False
    outputContent=False
    validImgFile=False
    validOrder=False
    validMode=False
    inpnum_content =False
    numrange_content =False
    maxnum_content = False
    float_gradient = False
    float_constant = False
    answers=dict()
    cont=''
    printOrder=''
    printMode=''
    diffLvl=''

    # Menu is prompted
    response=input(
    """\nPlease select your choice ('1','2','3','4','5','6','7'):
    1. Evaluate expression
    2. Sort expressions
    3. Print settings
    4. Sweet Math
    5. Explore Binary Trees
    6. Line Graphs
    7. Exit\nEnter Choice: """)

    # Implementation for option 1
    if response=='1':
        
        # Check if expression entered is valid and fully parenthesized
        while expError == False:
            exp=input('Please enter the expression you want to evaluate:\n')
            expError=ErrorCheck(exp).checkExpression()

        # Evaluate expression based on configuration settings        
        evaluation=ErrorCheck(exp).checkConfig()

        # Change float number to integer if it ends with 0 after decimal point
        if str(evaluation)[-2:]=='.0':
            evaluation=int(evaluation)

        # Print the expression tree
        print('\nExpression Tree:')

        ## Print accordingly if expression tree is set to print horizontally
        if pmode=='h':
            if order=='i':   ### Print in-order
                ParseTree(exp).buildParseTree().printInorder(0)
            elif order=='p': ### Print pre-order
                ParseTree(exp).buildParseTree().printPreorder(0)
            expList=[i for i in ParseTree(exp, 'tree2').buildParseTree().printInorder(0).splitlines() if i != '']

        ## Print accordingly if expression tree is set to print vertically
        elif pmode=='v':
            if order=='i':   ### Print in-order
                expList=[i for i in ParseTree(exp, 'tree2').buildParseTree().printInorder(0).splitlines() if i != '']
                VerticalTree('?').printAll(expList)
            elif order=='p': ### Print pre-order
                expList=[i for i in ParseTree(exp, 'tree2').buildParseTree().printPreorder(0).splitlines() if i != '']
                VerticalTree('?').printAll(expList)

        print (f'\nThe expression evaluates to:\n{evaluation}') ### Print the answer to expression

        # Build the tree diagram if print settings is horizontal and tree diagram is set to 'y'
        if treeDiag=='y' and pmode=='h':
            try:
                treeEdges=ConstructTree(expList).getEdgeList()
                while validImgFile==False:
                    filename=input('Please enter name for your tree image file: ')
                    validImgFile=ErrorCheck(imgFile=filename).checkImageFile()
                DrawTree(treeEdges,filename).saveTree()
            except:
                print('\nSorry, an error occurred and tree diagram could not be made for this expression.')

        input('\nPress any key to continue...')

    # Implementation for option 2
    elif response=='2':   
        
        # Validate input file
        while inputContent==False:
            inputFile=input('\nPlease enter input file: ')  
            inputContent=ErrorCheck(inputFile=inputFile).checkInputFile()

        # Validate output file
        while outputContent==False:
            outputFile=input('\nPlease enter output file: ')
            outputContent=ErrorCheck(inputFile=inputFile,outputFile=outputFile).checkOutputFile()

        # Create the evaluation report
        exps=Evaluate(inputFile).expList() 
        for exp in exps:
            ParseTree(exp).buildParseTree()
            evaluation=ErrorCheck(exp).checkConfig()
            answers[exp]=evaluation
        values=list(answers.values())
        report=Report(values, answers, outputFile).readReport()
        print(report)
        input('\nPress any key to continue...')

    # Implementation for option 3
    elif response == '3':
        
        # Prompt user for print order (in-order or pre-order)
        while validOrder==False:
            printOrder = input("Please enter the printing order ('i' for in-order, 'p' for pre-order): ")
            if printOrder in ['p', 'P']:
                order = 'p'
                print('Printing order is set to Pre-order.')
                validOrder=True
            elif printOrder in ['i','I']:
                order = 'i'
                print('Printing order set to In-order.')
                validOrder=True
            else:
                print("Invalid input! Enter only 'i' for in-order, 'p' for pre-order")

        # Prompt user for print mode (horizontal or vertical)
        if validOrder==True:
            while cont not in ['y', 'Y', 'n', 'N']:
                cont = input('\nWould you like to change advanced print mode settings? (y/n): ')
                if cont not in ['y', 'Y', 'n', 'N']:
                    print('Please only enter (y/n)!')
                elif cont in ['y','Y']:
                    while printMode not in ['h','H','v','V']:
                        printMode = input("\nPlease enter your printing mode ('v' for vertical, 'h' for horizontal): ")
                        if printMode in ['h','H']:
                            print('Print mode set to horizontal.')
                            pmode='h'  
                            treeDiag=''
                            validMode=True                         
                        elif printMode in ['v','V']:
                            print('Print mode set to vertical.')
                            pmode='v'
                            validMode=True
                        else:
                            print("Invalid input! Enter only 'v' for vertical, 'h' for horizontal")
            
                    # If user set print mode to horizontal, prompt user to decide 
                    # whether they want to save the expression tree diagram for option 1
                    if validMode==True and pmode=='h':
                        while treeDiag not in ['y','Y','n','N']:
                            treeDiag = input("\nWould you like to save expression tree as a diagram? (y/n): ")
                            if treeDiag in ['y','y']:
                                treeDiag='y'
                                print('Tree diagram will be saved in your given file.')
                            elif treeDiag in ['n','N']:
                                treeDiag='n'
                            else:
                                print('Please only enter (y/n)!')
                                
                elif cont in ['n','N']:
                    break

        input('\nPress any key to continue...')

    # Implementation for option 4               
    elif response == '4':

        # Print game instructions
        print('\n-----------------------------------------------------------------------------------------------------------------------------')
        print('- GAME INSTRUCTIONS                                                                                                         -')
        print('-----------------------------------------------------------------------------------------------------------------------------')
        print("- Welcome to Sweet Math! This is a fun math game which tests your foundation and speed in solving simple math equations.    -") 
        print("- In this game, you will be solving 10 simple math equations within a given time limit for each equation. Not all equations -")
        print("- are fully parenthesised. Thus, you would have to use your knowledge in BODMAS to solve the equations. You can press Enter -")
        print("- to skip a question but NO SCORES will be awarded. Your final score questions will be shown at the end of the game.        -")
        print("-                                                                                                                           -")
        print("- NOTE: PLEASE ROUND OFF YOUR ANSWERS TO 3 DECIMAL PLACES!!!                                                                -")
        print('-----------------------------------------------------------------------------------------------------------------------------')

        # Prompt user to choose the difficult of the game
        while diffLvl not in ['e','E','m','M','h','H']:
            
            diffLvl=input(
            '''\nChoose difficulty level: 
            - Easy (e)
            - Medium (m)
            - Hard (h)\nYour choice: ''')

            ## Construct the game based on the difficult level chosen by user (adjust time limit and complexitiy of equations)
            if diffLvl in ['e','E']:
                eqList=Expression(2).equationLists()
                timeLim=10
            elif diffLvl in ['m','M']:
                eqList=Expression(4).equationLists()
                timeLim=15
            elif diffLvl in ['h','H']:
                eqList=Expression(8).equationLists()
                timeLim=20
            else:
                print("Please only enter 'e','m','h'!")

        print(f'\nYou have a time limit of {timeLim}s for each question. All the best!')
        input('Press enter to begin the game...')

        # Store generated expressions and their answers into a HASH table
        expressions=eqList[0]
        answers=eqList[1]
        solutionTable = HashTable(10,expressions)
        for exp in expressions:
            solutionTable[exp]=answers[expressions.index(exp)]
        
        # Get final scores of user and leave comments
        score=SweetMath(solutionTable).evaluation(timeLim)
        if score<=5:
            print('Keep trying you will get there!')
        if score>5:
            print('Awesome! Keep it up :)')

        input('\nPress any key to continue...')

    # Implementation for option 5
    elif response == '5':
        #Check if input numbers are valid integers
        while inpnum_content == False:
            input_number = input('\nPlease enter a number. This will be your top Node:\n')
            inpnum_content = ErrorCheck(input3=input_number).int_input()
        while numrange_content == False:
            number_range =input('\nPlease enter a number. This will be the range of numbers in your binary tree:\n')
            numrange_content = ErrorCheck(input3=number_range).int_input()
        while maxnum_content ==False:
            maxnum = input('\nPlease enter the maximum number you want in your tree:\n')
            maxnum_content = ErrorCheck(input3=maxnum).int_input()
        # Input values in Binary Tree
        root = BST(int(input_number))
        v = Vertical(root)
        for _ in range(int(number_range)):
            root.insert(random.randint(0, int(maxnum)))
        #Prints out Binary Tree
        print("\nThis is your Binary Tree\n")
        root.drawtree()
        #Get number of levels a binary tree has
        levels = v.getlevelofTree(root)
        print(f'\nYour Binary tree has {levels} levels')
        # Get vertical sum of nodes in Binary Tree
        print('\nThe Vertical sum of nodes that are in the same vertical line is given below:')
        v.printVerticalSum()
        # Sums values of all nodes in Binary Tree 
        sum = v.totalSum(root)
        print(f'\nThe total sum of nodes in your Binary Tree is: {sum}')
        #Prints diagonal sum of nodes in Binary Tree
        v.diagonalSum(root)

    # Implementation for option 6
    elif response == '6':
        #Ask for inputs and Checks if inputs are valid floats
        while float_gradient == False:
            x = input('\nPlease enter gradient:')
            float_gradient = ErrorCheck(float_input=x).float_inputcheck()
        while float_constant == False:
            c = input('\nPlease enter a number (constant):')
            float_constant = ErrorCheck(float_input=c).float_inputcheck()
        # Draw the Graph according to input
        g = GraphTurtle()
        g.drawAxis()
        g.drawLinearGraph(float(x),float(c))


    # If user choice is not between the 7 options, prompt error
    elif response not in ('1','2','3','4','5','6','7'):
        print('Invalid input!') 

# if user enters 7, program is exited and ending message is shown
print('\nBye, thank you for using ST1507 DSAA: Expression Evaluator & Sorter!')