# Name: Jumana Haseen
# StudentID: 2021627
# Class: DAAA/FT/2B/02

# Import libraries
import random
import math

# Expression class to generate simple math expressions
class Expression:
    OPS = ['+', '-', '*', '/'] #operators used
    GROUP_PROB = 0.3
    MIN_NUM, MAX_NUM = 1, 20   #range of number

    def __init__(self, maxNumbers, _maxdepth=None, _depth=0):
        """
        maxNumbers has to be a power of 2
        """
        if _maxdepth is None:
            _maxdepth = math.log(maxNumbers, 2) - 1
        if _depth < _maxdepth and random.randint(0, _maxdepth) > _depth:
            self.left = Expression(maxNumbers, _maxdepth, _depth + 1)
        else:
            self.left = random.randint(Expression.MIN_NUM, Expression.MAX_NUM)
        if _depth < _maxdepth and random.randint(0, _maxdepth) > _depth:
            self.right = Expression(maxNumbers, _maxdepth, _depth + 1)
        else:
            self.right = random.randint(Expression.MIN_NUM, Expression.MAX_NUM)
        self.max=maxNumbers
        self.grouped = random.random() < Expression.GROUP_PROB
        self.operator = random.choice(Expression.OPS)

    # Printing of equation
    def __str__(self):
        s = '{0!s} {1} {2!s}'.format(self.left, self.operator, self.right)
        if self.grouped:
            return '({0})'.format(s)
        else:
            return f'{s}'

    # Get the generated expressions and its respective answers
    def equationLists(self):
        expressions=list()
        answers=list()
        while len(expressions)!=10:
            try:
                exp=Expression(self.max)
                ans=round(eval(f'{exp}'),3)
                if str(ans)[-2:]=='.0':
                    ans=str(int(ans))
                expressions.append(exp)
                answers.append(ans)
            except:
                pass
        return expressions, answers