def weight_on_planets():
   earth=float(input('What do you weigh on earth? '))
   
   print('\nOn Mars you would weigh %f.2 pounds. \
   	     \nOn Jupiter you would weigh %f.2 pounds.' \
   	     %(earth*0.38, earth*2.34))
   
   
if __name__ == '__main__':
   weight_on_planets()