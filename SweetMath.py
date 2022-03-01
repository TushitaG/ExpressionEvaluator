# Name: Jumana Haseen
# StudentID: 2021627
# Class: DAAA/FT/2B/02

# Import libraries
import time
import msvcrt

# Math game class to generate the SweetMath game.
class SweetMath:

    def __init__(self, solutions):
        self.sol=solutions
        self.exp=solutions.keys
        self.ans=solutions.buckets

    # Set time limit for each equation
    def timer(self, caption, timeout=10):
        start_time = time.time()
        print(caption)
        inpt = ''
        while True:
            if msvcrt.kbhit():  # Check if a key press is waiting.
                # Check which key was pressed and turn it into a unicode string.
                char = msvcrt.getche().decode(encoding='utf-8')
                
                # If enter was pressed, return the inpt.
                if char in ('\n', '\r'): # enter key
                    return inpt

                elif char=='\b':
                    inpt=inpt[:-1]
                
                # If another key was pressed, concatenate with previous chars.
                elif char >= ' ': # Keys greater or equal to space key.
                    inpt += char
           
            # If time is up, return the inpt.
            if time.time()-start_time > timeout:
                print('Time is up.')
                inpt='---Not answered---'
                return inpt

    # Generate game and evaluate user answer
    def evaluation(self,timeLim):
        score=0
        ans=''
        for i in range(len(self.exp)):
            ans = self.timer(f'\nEquation {i+1}: {self.exp[i]}', timeout=timeLim)
            print(f'Your answer : {ans}')

            while (ans.replace('.','')).replace('-','').isdigit()==False and ans!='---Not answered---' and ans!='':
                print('Error! Please only enter float or integer.')
                ans = self.timer(f'\nEquation {i+1}: {self.exp[i]}', timeout=timeLim)
                print(f'Your answer : {ans}')
                
            if str(self.sol[self.exp[i]])==ans:
                print('Correct answer, Well done!')
                score=score+1
            elif ans=='':
                print('Question is skipped, no scores will be awarded')
                print(f'The correct answer is: {self.sol[self.exp[i]]}')
                pass
            elif str(self.sol[self.exp[i]])!=ans:
                print(f'Incorrect answer... The correct answer is: {self.sol[self.exp[i]]}')
        
        print(f'\nYour final score: {score}/10')
        return score

