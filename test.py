import re
import sys
replacements = {
    '^': '**',
}

allowed_words = [
    'x',
]
def testmathexp(mathexp):
   mathexp = mathexp.replace(' ', '')
   if mathexp == "":
       raise ValueError("please enter Function in terms of x in lowercase ")
   for word in re.findall('[a-zA-Z_]+', mathexp):
       if word not in allowed_words:
           raise ValueError(
               '"{}" is forbidden to use in math expression'.format(word)
           )
   toMatch = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
   matched = re.match(toMatch, mathexp)
   if not matched:
       raise ValueError("Invalid Expression")

   mathexp=mathexp.replace('^','**')
   return mathexp

def testnumber(num):
    if num == "":
        raise ValueError("Enter the limits please")
    try:
        a=int(num)
        return a
    except:
        raise ValueError("Please enter numbers")

def testlimits(min,max):
    if min >= max:
        raise ValueError("lower limit should be smaller than upper limit")
def testDivisionByZero(expression, minValue, maxValue):
    if expression.find('/x') != -1 and minValue <= 0 and maxValue >= 0:
        return False
    return True