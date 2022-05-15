import matplotlib.pyplot as plt
import numpy as np
import test
import re
import sys
class plot:
   def __init__(self,mathex,low,upp):
       self.lineEdit = test.testnumber(low)
       self.lineEdit_2 = test.testnumber(upp)
       test.testlimits(self.lineEdit, self.lineEdit_2)
       self.lineEdit_3 = test.testmathexp(mathex)
       #try:
        #   e = self.FuncSubstitute(1)
       #except Exception:
        #   raise ValueError("Invalid Function")

   def FuncSubstitute(self, x):
        val = eval(self.lineEdit_3)  # built in function to substitute easily
        return val
    # generate X-Coordnates and Y_Coordinates Lists


   def GenerateFunc(self):
      x_Coor = []
      y_Coor = []
      testZeroDiv = test.testDivisionByZero(self.lineEdit_3, self.lineEdit, self.lineEdit_2)
      for i in range(self.lineEdit, self.lineEdit_2):
           x_Coor.append(i)
           if testZeroDiv == False and i == 0:  # put the y-value with infinity if(x is a denominator and x == 0)
               y_Coor.append(float('inf'))
           else:
               y_Coor.append(self.FuncSubstitute(i))

      return x_Coor, y_Coor

    # Plot the function using matplot


   def plotFunction(self):
      x_Coor, y_Coor = self.GenerateFunc()
      plt.plot(x_Coor, y_Coor, color="red", linewidth=1.5, label=self.lineEdit_3)
      plt.xlabel("X")
      plt.ylabel("F(X)")
      plt.style.use("seaborn-dark")
      plt.grid()
      plt.show()
