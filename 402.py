def rounder(numtoround , numdec):
     return int(numtoround * 10** numdec +0.5 )/ 10.0** numdec 
     

numberround = input('enter a number to be rounded: ');
decimals = input('enter the amount of decimals: '); 

print ('The number {0} rounded to {1} decimals is:{2}'.format(numberround, decimals, rounder(numberround, decimals)))
