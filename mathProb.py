import matplotlib.pyplot as plt
import time
import numpy as np

def odd_or_even(x):
   num = x
   iterat = 0
   xpoint = np.array([])
   ypoint = np.array([])
   
   while num != 1:
      #time.sleep(0.1)
      iterat += 1
      
      if num % 2 == 0:
         num = int(num / 2)
         print(f"Num: {num} even")
         ypoint = np.append(ypoint, num)
         
      elif num % 2 != 0:
         num = int((num * 3) + 1)
         print(f"Num: {num} odd")
         ypoint = np.append(ypoint, num)

      xpoint = np.append(xpoint, iterat)
 
   plt.plot(xpoint, ypoint)
   plt.show()

   odd_or_even(int(input("Write a positive number: ")))      

